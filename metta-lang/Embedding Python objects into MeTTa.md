# Embedding Python objects into MeTTa

## `py-atom`

Introducing tokens for grounded atoms allows for both convenient syntax and direct representation of expressions with corresponding grounded atoms in a Space. However, wrapping all functions of rich Python libraries can be not always desirable. There is a way to invoke Python objects such as functions, classes, methods or other statements from MeTTa without additional Python code wrapping these objects into atoms.

`py-atom` allows obtaining a grounded atom for a Python object imported from a given module or submodule. Let us consider usage of `numpy` as an example, which should be installed. For instance, the absolute value of a number in MeTTa can be calculated by employing the `absolute` function from the `numpy` library:

```
! ((py-atom numpy.absolute) -5) ; 5
```

Here, `py-atom` imports `numpy` library and returns an atom associated with the `numpy.absolute` function.

It is possible to designate types for the grounded atom in `py-atom`. For convenience, one can associate the result of `py-atom` with a token using `bind!`:

```
! (import! &self py_ops)
! (bind! abs (py-atom numpy.absolute))
! (+ (abs -5) 10) ; np.int64(15)
```

We specify here that the constructed grounded operation can accept an argument of type `Number` and its result will be of `Number` type.

When `(abs -5)` is executed, it triggers a call to `absolute(-5)`. It can be seen that the results of executing Python objects imported via `py-atom` can then be directly utilized in other MeTTa expressions.

`py-atom` can actually execute some Python code, which shouldn't be a statement like `x = 42`, but should be an expression, which evaluation produces a Python object. In the following example, `(py-atom "[1, 2, 3]")` produces a Python list, which then passed to `numpy.array`.

```
! (bind! np-array (py-atom numpy.array))
! (np-array (py-atom "[1, 2, 3]")) ; array([1, 2, 3])
```

`py-atom` can be applied to functions accepting keyword arguments. Constructed grounded atoms will also support `Kwargs` ([mentioned earlier](https://metta-lang.dev/docs/learn/tutorials/python_use/tokenizer.html#kwargs-for-operationatom)), which allows for passing only the required arguments to the function while skipping arguments with default values. For example, there is `numpy.arange` in NumPy, which returns evenly spaced values within a given interval. `numpy.arange` can be called with a varying number of positional arguments:

```
! (bind! np-arange (py-atom numpy.arange)) ; ()
! (np-arange 4) ; array([0, 1, 2, 3])
! (np-arange (Kwargs (step 2) (stop 8))) ; array([0, 2, 4, 6])
! (np-arange (Kwargs (start 2) (stop 10) (step 3))) ; array([2, 5, 8])
```

## `py-dot`

What if we wish to call functions from a submodule, say `numpy.random`? Accessing these functions via something like `(py-atom numpy.random.randint)` will work. However, it would be more efficient to get `numpy.random` itself as a Python object and access other objects in it. `py-dot` is introduced to carry out this operation.

```
! (bind! np-rnd (py-atom numpy.random))
! ((py-dot np-rnd randint) 25)
```

In this case `py-dot` operates with two arguments: it takes the first argument, which is the grounded atom wrapping a Python object, and then searches for the value of an attribute within that object based on the name provided in the second argument.

This second argument can also contain objects in submodules. In the following example, we wrap `numpy` in the grounded atom:

```
! (bind! np (py-atom numpy))
! ((py-dot np abs) -5)
! ((py-dot np random.randint) -25 0)
! ((py-dot np abs) ((py-dot np random.randint) -25 0))
```

Here, when `(py-dot np random.randint)` is executed, it takes `numpy` object and searches for `random` in it and then for `randint` in `random`. The overall result is the grounded operation wrapping `numpy.random.randint`, which is then applied to some argument. Similar to `py-atom`, `py-dot` also permits the designation of types for the function, and supports `Kwargs` for arguments specification.

Binding `np` to `(py-atom numpy)` and accessing functions in it via `(py-dot np abs)` looks not more convenient than just using `(py-atom numpy.abs)`, but is slightly more efficient if `numpy.abs` is accessed multiple times.

`py-dot` works for any Python object - not only modules:

```
! ((py-dot "Hello World" swapcase)) ; "hELLO wORLD"
```

Notice the additional brackets to call `swapcase`. The equivalent Python code is `"Hello World".swapcase()`, which also contains `()`. One more pair of brackets in MeTTa is needed, because `py-dot` is also a function.

Let us consider another example.

```
! ((py-dot (py-atom "{5: \'f\', 6: \'b\'}") get) 5)
```

Here, a dictionary `{5: 'f', 6: 'b'}` is created by `py-atom`, and then the value corresponding to the key `5` is retrieved from this dictionary using `get` accessed via `py-dot`.

## `py-list`, `py-tuple`, `py-dict`

While it is possible to create Python lists and dictionaries using code evaluation by `py-atom`, it can be desirable to construct these data structures by combining atoms in MeTTa.

In this context, since passing dictionaries, lists or tuples as arguments to functions in Python is very common, such dedicated functions as `py-dict`, `py-list` and `py-tuple` were introduced.

```
! ((py-atom max) (py-list (-5 5 -3 10 8))) ; 10
! ((py-atom numpy.inner)
     (py-list (1 2)) (py-list (3 4))) ; 1 * 3 + 2 * 4 = 11
```

In this example, `py-list` generates three Python lists: `[-5, 5, -3, 10, 8]` , `[1,2]` and `[3,4]`, which are passed to `max` and `numpy.inner`.

Of course, one can use `py-dict`, `py-list`, and `py-tuple` independently - not just as function arguments:

```
! (py-dict (("a" "b") ("b" "c"))) ; creates a dict {"a":"b", "b":"c"}
! (py-tuple (1 5)) ; creates a tuple (1, 5)
! (py-list (1 (2 (3 "3")))) ; creates a nested list [1, [2, [3, '3']]]
```