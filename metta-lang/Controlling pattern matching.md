Both standard and custom functions in MeTTa can have `Atom`-typed arguments, which will not be reduced before these functions are evaluated. But we may want to call them on a result of another function call. What is the best way to do this? Before answering this question, let us consider `match` in more detail.

## Type signature of the `match` function

Pattern matching is the core operation in MeTTa, and it is implemented using the `match` function, which locates all atoms in the given Space that match the provided pattern and generates the output pattern.

Let us recall that the `match` function has three arguments:

- a grounded atom referencing a Space;
- a pattern to be matched against atoms in the Space (query);
- an output pattern typically containing variables from the input pattern.

Consider the type of `match`:

```
! (get-type match)
```

The second and the third arguments are of `Atom` type. Thus, the input and the output pattern are passed to `match` as is, without reduction. Preventing reduction of the input pattern is essentially needed for the possibility to use any pattern for matching. The output pattern is instantiated by `match` and returned, and only then it is evaluated further by the interpreter.

## in-and-out behavior of `match`

In the following example, `(Green $who)` is evaluated to `True` for `$who` bound to `Tod` due to the corresponding equality.

```
(Green Sam)
(= (Green Tod) True)
! ($who (Green $who)) ; (Tod True)
! (match &self (Green $who) $who) ; Sam
```

However, `(Green $who)` is not reduced when passed to `match`, and the query returns `Sam`, without utilizing the equality because `(Green Sam)` is added to the Space.

Let us verify that the result of `match` will be evaluated further. In the following example, `match` first finds two entries satisfying the pattern `(Green $who)` and instantiates the output pattern on the base of each of them, but only `(Frog Sam)` is evaluated to `True` on the base of one available equality, while `(Frog Tod)` remains unreduced.

```
(Green Sam)
(Green Tod)
(= (Frog Sam) True)
! (match &self (Green $who) (Frog $who)) ; [True, (Frog Tod)]
```

We can verify that instantiation of the output pattern happens before its evaluation:

```
(Green Sam)
(= (Frog Sam) True)
! (match &self (Green $who) (quote (Frog $who)))
```

Here, `(Green $who)` is matched against `(Green Sam)`, `$who` gets bound to `Sam`, and then it is substituted to the output pattern yielding `(quote (Frog Sam))`, in which `(Frog Sam)` is not reduced further to `True`, because `quote` also expects `Atom`. Thus, `match` can be thought of as transformation of the input pattern to the output pattern. It performs no additional evaluation of patterns by itself.

Returning output patterns with substituted variables before further evaluation is very convenient for nested queries. Consider the following example:

```
(Green Sam)
(Likes Sam Emi)
(Likes Tod Kat)
! (match &self (Green $who)
    (match &self (Likes $who $x) $x))
! (match &self (Green $who)
    (match &self (Likes $boo $x) $x))
! (match &self (Likes $who $x)
    (match &self (Green $x) $x))
! (match &self (Likes $who $x)
    (match &self (Green $boo) $boo))
```

The output of the outer query is another query. The inner query is not evaluated by itself, but instantiated as the output of the outer query.

- In the first case, `$who` gets bound to `Sam` and the pattern in the second query becomes `(Frog Sam $x)`, which has only one match, so the output is `Emi`.
- In the second case, `$who` is not used in the inner query, and there are two results, because the pattern of the second query remains `(Likes $boo $x)`.
- In the third case, there are no results, because the outer query produces two results, but neither `(Green Emi)` nor `(Green Kat)` are in the Space.
- In the last case, `Sam` is returned two times. The outer query returns two results, and although its variables are not used in the inner query, it is evaluated twice.

## Patterns are not type-checked

Functions with `Atom`-typed parameters can accept atoms of any other type, including badly typed expressions, which are not supposed to be reduced. As it was mentioned earlier, this behavior can be useful in different situations. Indeed, why couldn't we, say, quote a badly typed expression as an incorrect example?

It should be noted, though, that providing specific types for function parameters and simultaneously indicating that the corresponding arguments should not be reduced could be useful in other cases. Unfortunately, it is currently not possible to provide a specific type and a metatype simultaneously (which is [one of the known issues](https://github.com/trueagi-io/hyperon-experimental/issues/177)).

At the same time, `match` is a very basic function, which should not be restricted in its ability to both accept and return "incorrect" expressions. Thus, one should keep in mind that `match` does not perform type-checking on its arguments, which is intentional and expected.

The following program contains a badly typed expression, which can still be pattern-matched (and `match` can accept a badly typed pattern):

```
(+ 1 False)
! (match &self (+ 1 False) OK) ; OK
! (match &self (+ 1 $x) $x) ; False
```

It can be useful to deal with "wrong" MeTTa programs on a meta-level in MeTTa itself, so this behavior of `match` allows us to write code that analyzes badly typed expressions within MeTTa.

## Type of `=`

MeTTa programs typically contain many equalities. But is there a guarantee that the function will indeed return the declared type? This is achieved by requiring that both parts of equalities are of the same type. Consider the following code:

```
(: foo (-> Number Bool))
(= (foo $x) (+ $x 1))
! (get-type (foo $x)) ; Bool
! (get-type (+ $x 1)) ; Number
! (get-type =) ; (-> $t#nnnn $t#nnnn Atom)
! (= (foo $x) (+ $x 1)) ; BadType
```

We declared the type of `foo` to be `(-> Number Bool)`. On the base of this definition, the type of `(foo $x)` can be reduced to `Bool`, which is the expected type of its result. However, the type of its body `(+ $x 1)` is reduced to `Number`. If we get the type of `=`, we will see that both its arguments should be of the same type. The result type of `=` is `Atom`, since it is not a function (unless someone adds an equality over equalities, which is permissible). If one tries to "execute" this equality, it will indeed return the type error.

Programs can contain badly typed expressions as we discussed earlier. However, this may permit badly defined functions. `! (pragma! type-check auto)` can be used to enable automatic detection of such errors:

```
! (pragma! type-check auto) ; ()
(: foo (-> Number Bool))
(= (foo $x) (+ $x 1)) ; BadType
```

This pragma option turns on type-checking of expressions before adding them to the Space (without evaluation of the expression itself).

## `let`'s evaluate

Sometimes we need to evaluate an expression before passing it to a function, which expects `Atom`-typed arguments. What is the best way to do this?

One trick could be to write a wrapper function like this

```
(= (call-by-value $f $arg)
   ($f $arg))
! (call-by-value quote (+ 1 2)) ; (quote 3)
```

Arguments of this function are not declared to be of `Atom` type, so they are evaluated before the function is called. Then, the function simply passes its evaluated argument to the given function. However, it is not needed to write such a wrapper function, because there is a more convenient way with the use of operation `let` from stdlib.

`let` takes three arguments:

- a variable atom (or, more generally, a pattern)
- an expression to be evaluated and bound to the variable (or, more generally, matched against the pattern in the first argument)
- the output expression (which typically contains a variable to be substituted)

```
! (let $x (+ 1 2) (quote $x)) ; (quote 3)
(: Z Nat)
! (get-metatype (get-type Z)) ; (get-type Z) is Expression
! (let $x (get-type Z) (get-metatype $x)) ; Nat is Symbol
```

One may also want to evaluate some subexpression before constructing an expression for pattern-matching

```
(= (age Bob) 5)
(= (age Sam) 8)
(= (age Ann) 3)
(= (age Tom) 5)
(= (of-same-age $who)
   (let $age (age $who)
        (match &self (= (age $other) $age)
               $other)))
! (of-same-age Bob) ; [Bob, Tom]
; without `of-same-age`:
! (let $age (age Bob)
       (match &self (= (age $other) $age)
              $other)) ; also [Bob, Tom]
! (match &self (= (age $other) (age Bob))
         $other) ; does not pattern-match
; evaluating the whole pattern is a bad idea
! (let $pattern (= (age $other) (age Bob))
       $pattern) ; [(= 5 5), (= 8 5), (= 5 5), (= 3 5)]
! (let $pattern (= (age $other) (age Bob))
       (match &self $pattern $other)) ; does not pattern-match
```

It can be seen that `let` helps to evaluate `(age Bob)` before constructing a pattern for retrieval. However, evaluating the whole pattern is typically a bad idea. That is why patterns in `match` are of `Atom` type, and `let` is used when something should be evaluated beforehand.

As was remarked before, `let` can accept a pattern instead of a single variable. More detailed information on `let` together with other functions from stdlib are provided in [the next tutorial](https://metta-lang.dev/docs/learn/tutorials/stdlib_overview/intro.html).

## Unit type

`Unit` is a type that has exactly one possible value `unit` serving as a return value for functions, which return "nothing". However, from the type-theoretic point of view, mappings to the empty set do not exist (they are non-constructive), while mappings to the one-element set do exist, and returning the only element of this set yields zero information, that is, "nothing". This is equivalent to `void` in such imperative languages as C++.

In MeTTa, the empty expression `()` is used for the unit value, which is the only instance of the type `(->)`. A function, which doesn't return anything meaningful but which is still supposed to be a valid function, should return `()` unless a custom unit type is defined for it.

In practice, this `()` value is used as the return type for grounded functions with side effects (unless these side effects are not described in a special way, e.g., with monads). For example, the function `add-atom` adds an atom to the Space, and returns `()`.

When it is necessary to execute such a side-effect function and then to return some value, or to chain it with subsequent execution of another side-effect function, it is convenient to use the following construction based on `let`: `(let () (side-effect-function) (evaluate-next))`. If `(side-effect-function)` returns `()`, it is matched with the pattern `()` in `let`-expression (one can use a variable instead of `()` as well), and then `(evaluate-next)` is executed.

Let us consider a simple knowledge base for a personal assistant system. The knowledge base contains information about the tasks the user is supposed to do. A new atom in this context would be a new task.

```
(= (message-to-user $task)
   (Today you have $task))
(= (add-task-and-notify $task)
    (let () (add-atom &self (TASK $task))
            (message-to-user $task))
)
! (get-type add-atom) ; (-> hyperon::space::DynSpace Atom (->))
! (add-task-and-notify (Something to do))
! (match &self (TASK $t) $t) # (Somthing to do)
```

The `add-task-and-notify` function adds a `$task` atom into the current Space using the `add-atom` function and then calls another function which returns a message to notify the user about the new task. Please, notice the type signature of `add-atom`.