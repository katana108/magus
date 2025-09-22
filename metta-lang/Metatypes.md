# Metatypes

## Peeking into metatypes

In MeTTa, we may need to analyze the structure of atoms themselves. The [tutorial](https://metta-lang.dev/docs/learn/tutorials/eval_intro/main_concepts.html#atom-kinds-and-types) starts with introducing four kinds of atoms - `Symbol`, `Expression`, `Variable`, `Grounded`. We refer to them as **metatypes**. One can use `get-metatype` to retrieve the metatype of an atom

```
! (get-metatype 1) ; Grounded
! (get-metatype +) ; Grounded
! (get-metatype (+ 1 2)) ; Expression
! (get-metatype a) ; Symbol
! (get-metatype (a b)) ; Expression
! (get-metatype $x) ; Variable
```

How to process atoms depending on their metatypes is discussed in another tutorial. In this tutorial, we discuss one particular metatype, which is widely utilized in MeTTa to control the order of evaluation. You should have noticed that arguments of some functions are not reduced before the function is called. This is true for `get-type` and `get-metatype` functions. Let us check their type signatures:

```
! (get-type get-type) ; (-> Atom Atom)
! (get-type get-metatype) ; (-> Atom Atom)
```

Here, `Atom` is a supertype for `Symbol`, `Expression`, `Variable`, `Grounded`. While metatypes can appear in ordinary type signatures, they should not be assigned explicitly, e.g. `(: a Expression)`, except for the following special case.

`Atom` is treated specially by the interpreter - if a function expects an argument of `Atom` type, this argument is not reduced before passing to the function. This is why, say, `(get-metatype (+ 1 2))` returns `Expression`. It is worth noting that `Atom` as a return result will have no special effect. While `Atom` as the return type could prevent the result from further evaluation, this feature is not implemented in the current version of MeTTa.

Using arguments of `Atom` type is essential for meta-programming and self-reflection in MeTTa. However, it has a lot of other more common uses.

## Quoting MeTTa code

We encountered error expressions. These expressions can contain unreduced atoms, because `Error` expects the arguments of `Atom` type:

```
! (get-type Error) ; (-> Atom Atom ErrorType)
! (get-metatype Error) ; just Symbol
! (get-type (Error Foo Boo)) ; ErrorType
! (Error (+ 1 2) (+ 1 +)) ; arguments are not evaluated
```

`Error` is not a grounded atom, it is just a symbol. It doesn't even have defined equalities, so it works just an expression constructor, which prevents its arguments from being evaluated and which has a return type, which can be used to catch errors.

Another very simple constructor from stdlib is `quote`, which is defined just as `(: quote (-> Atom Atom))`. It does nothing except of wrapping its argument and preventing it from being evaluated.

```
! (get-type quote)
! (quote (+ 1 2))
! (get-type if)
```

Some programming languages introduce `quote` as a special symbol known by the interpreter (otherwise its argument would be evaluated). Consequently, any term should be quoted, when we want to avoid evaluating it. However, `quote` is an ordinary symbol in MeTTa. What is specially treated is the `Atom` metatype for arguments. It appears to be convenient not only for extensive work with MeTTa programs in MeTTa itself (for code generation and analysis, automatic programming, meta-programming, genetic programming and such), but also for implementing traditional control statements.

## `if` under the hood

As was mentioned in the [tutorial](https://metta-lang.dev/docs/learn/tutorials/eval_intro/recursion.html#conditional-statements), the `if` statement in MeTTa works much like if-then-else construction in any other language. `if` is not an ordinary function and typically requires a special treatment in interpreters or compilers to avoid evaluation of branches not triggered by the condition.

However, its implementation in MeTTa can be done with the following equalities

```
(= (if True $then $else) $then)
(= (if False $then $else) $else)
```

The trick is to have the type signature with the first argument typed `Bool`, and the next two arguments typed `Atom`. The first argument typed `Bool` can be an expression to evaluate like `(> a 0)`, or a `True`/`False` value. The `Atom`-types arguments `$then` and `$else` will not be evaluated while passing into the `if` function. However, once the `if`-expression has been reduced to either of them, the interpreter will chain its evaluation to obtain the final result.

Consider the following example

metta sandbox

If you comment out the type definition, then the program will go into an infinite loop trying to evaluate all the arguments of `my-if`. Lazy model of computation could automatically postpone evaluation of `$then` and `$else` expressions until they are not required, but it is not currently implemented.

Can you imagine how a "sequential and" function can be written, which evaluates its second argument, only if the first argument is `True`?

metta sandbox

Apparently, in the proposed setting, the first argument should be evaluated, so its type should be `Bool`, while the second argument shouldn't be immediately evaluated. What will be the whole solution?

## Transforming expressions

One may want to use `Atom`-typed arguments not only for just avoiding computations or quoting expressions, but to modify them before evaluation.

Let us consider a very simple example with swapping the arguments of a function. The code below will give `-7` as a result

```
(: swap-arguments-atom (-> Atom Atom))
(= (swap-arguments-atom ($op $arg1 $arg2))
   ($op $arg2 $arg1)
)
! (swap-arguments-atom (- 15 8))
```

At the same time, the same code without typing will not work properly and will return `[(swap-arguments 7)]`, because `(- 15 8)` will be reduced by the interpreter before passing to the `swap-arguments` and will not be pattern-matched against `($op $arg1 $arg2)`

```
(= (swap-arguments ($op $arg1 $arg2))
   ($op $arg2 $arg1)
)
! (swap-arguments (- 15 8))
```

One more example of using the `Atom` type is comparing expressions

```
; `atom-eq` returns True, when arguments are identical
; (can be unified with the same variable)
(: atom-eq (-> Atom Atom Bool))
(= (atom-eq $x $x) True)

; These expressions are identical:
! (atom-eq (+ 1 2) (+ 1 2))

; the following will not be reduced because the expressions are not the same 
; (even though the result of their evaluation would be)
! (atom-eq 3 (+ 1 2))
```