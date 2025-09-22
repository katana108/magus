# Concrete types

## Types of symbols

Atoms in MeTTa are typed. Types of atoms are also represented as atoms (typically, symbolic atoms and expressions). Expressions of the form `(: <atom> <type>)` are used to assign types. For example, to designate that the symbol atom `a` has a custom type `A` one needs to add the expression `(: a A)` to the space (program).

Note that since `A` here is a symbol atom, it can also have a type, e.g., `(: A Type)`. The symbol atom `Type` is conventionally used in MeTTa to denote the type of type atoms. However, it is not assigned automatically. That is, declaration `(: a A)` doesn't force `A` to be of type `Type`.

When an atom has no assigned type, it has `%Undefined%` type. The value of `%Undefined%` type can be type-checked with any type required.

One can check the type of an atom with `get-type` function from stdlib.

```
(: a A)
(: b B)
(: A Type)

! (get-type a) ; A
! (get-type b) ; B
! (get-type c) ; %Undefined%
! (get-type A) ; Type
! (get-type B) ; %Undefined%
```

Here, we declared types `A` and `B` for `a` and `b` correspondingly, and type `Type` for `A`. `get-type` returns the declared types or `%Undefined%` if no type information is provided for the symbol.

## Types of expressions

Consider the following program.

```
(: a A)
(: b B)
! (get-type (a b)) ; (A B)
```

The type of expression `(a b)` will be `(A B)`. The type of a tuple is a tuple of types of its elements. However, what if we want to apply a function to an argument? Usually, we want to check if the function argument is of appropriate type. Also, while function applications themselves are expressions, they are transformed in the course of evaluation, and the result has its own type. Basically, we want to be able to transform (or reduce) types of expressions before or without transforming expressions themselves.

Arrow `->` is a built-in symbol of the type system in MeTTa, which is used to create a function type, for example `(: foo (-> A B))`. This type signature says that `foo` can accept an argument of type `A` and its result will be of type `B`:

```
(: a A)
(: foo (-> A B))
! (get-type (foo a)) ; B
```

Let us note that

- We didn't provide a body for `foo`, so `(foo a)` is not reduced at all, and its type `B` is derived purely from the types of `foo` and `a`. It doesn't matter whether `foo` is a real function or a data constructor.
- Equality queries themselves don't care about the position of the function symbol in the tuple, and the following code is perfectly correct

```
(= ($1 infix-f $2) ($2 $1))
! (match &self (= (1 infix-f 2) $r) $r)
```

However, reduction of the type of a tuple is performed if its **first** element has an arrow (function) type. For convenience and by convention, the first element in a tuple is treated specially for function application.

## Type-checking

Types can protect against incorrectly constructed expressions including misuse of a function, when we want it to accept arguments of a certain type.

```
; This function accepts an atom of type A and returns an atom of type B
(: foo (-> A B))
(: a A)
(: b B)

! (foo a) ; no error
! (get-type (foo b)) ; no result
! (b foo) ; notice: no error
! (get-type (b foo)) ; (B (-> A B))
! (foo b) ; type error
```

We didn't define an equality for `foo`, so `(foo a)` reduces to itself. However, an attempt to evaluate `(foo b)` results in the error expression. When we try to get the type of this expression with `(get-type (foo b))`, the result is empty meaning that this expression has no valid type.

Notice that evaluation of `(b foo)` doesn't produce an error. The arrow type of `foo` in the second position of the tuple doesn't cause transformation of its type. Indeed, `(get-type (b foo))` produces `(B (-> A B))`.

## Gradual typing

Let us consider what types will expressions have, when some of their elements are `%Undefined%`. Run the following program to check the currently implemented behavior

```
(: foo (-> A B))
(: a A)
! (get-type (foo c))
! (get-type (g a))
```

Note that `g` and `c` are of `%Undefined%` type, while `foo` and `a` are typed. The result can be different depending on which type is not defined, of the function or its argument.

## Multiple arguments

Functions can have more than one argument. In their type signature, types of their parameters are listed first, and the return type is put at the end much like for functions with one argument.

The wrong order of arguments with different types as well as the wrong number of arguments will render the type of the whole expression to be empty (invalid).

metta sandbox

Here, the atom `c` is of `%Undefined%` type and it can be matched against an atom of any other type. Thus, `(foo2 a c)` will not produce an error. However, `(foo2 c)` will not work because of wrong arity.

Also notice that it is not necessary to define an instance of type `C`. `foo2` by itself acts as a constructor for this type.

What will be the type of a function with zero arguments? Its type expression will have only the return type after `->`, e.g.

```
(: a A)
(: const-a (-> A))
(= (const-a) a)
```

## Nested expressions

Types of nested expressions are inferred from innermost expressions outside. You can try nesting typed expressions in the sandbox below and see what goes wrong.

metta sandbox

Note that type signatures can be nested expressions by themselves:

```
(: foo-pair (-> (A B) C))
(: a A)
(: b B)

! (get-type (foo-pair a b)) ; empty
! (get-type (foo-pair (a b))) ; C
```

As was mentioned above, an arrow type of the atom, which is not the first in the tuple, will not cause type reduction. Thus, one may apply a function to another function (or a data constructor):

```
(: foo (-> (-> A B) C))
(: bar (-> A B))
(: a A)

! (get-type (foo bar)) ; C
! (get-type (foo (bar a))) ; empty
```

Here, the type of `bar` matches the type of the first parameter of `foo`. Thus, `(foo bar)` is a well-typed expression, which overall type corresponds to the return type of `foo`, namely, `C`.

`(foo (bar a))`, in turn, is badly typed, because the type of `(bar a)` is reduced to `B`, which does not correspond to `(-> A B)` expected by `foo`.

Similarly, the return type of a function can be an arbitrary expression including arrow types. Try to construct a well-typed expression involving all the following symbols

metta sandbox

We intentionally don't provide function bodies here to underline that typing imposes purely structural restrictions on expressions, which don't require understanding the semantics of functions. In the example above, `foo` accepts an atom of type `C`. Thus, `(foo c)` is well-typed, and its reduced type is `(-> A B)`. This is an arrow type meaning that we can put this expression at the first position of a tuple (function application), and it will expect an atom of type `A`. Thus, `((foo c) a)` should be well-typed, and its reduced type will be `B`. Thus, we can apply `bar` to it. Will `(bar ((foo c) a))` be indeed well-typed?

## Grounded atoms

Grounded atoms are also typed. One can check their types with `get-type` as well:

```
! (get-type 1) ; Number
! (get-type 1.1) ; Number
! (get-type +) ; (-> Number Number Number)
! (get-type (+ 1 2.1)) ; Number
```

As the example shows, `1` and `1.1` both are of `Number` type, although their data-level representation can be different. `+` accepts two arguments of `Number` type and returns the result of the same type. Thus, `Number` is repeated three times in its type signature.

Let us note once again that the argument of `get-type` is not evaluated, and `get-type` returns an inferred type of expression. In particular, when we try to apply `+` to the argument of a wrong type, the result is the error expression (which by itself is well-typed), but `get-type` returns the empty result instead of returning the type of the error message:

```
(: a A)
! (get-type (+ 1 a)) ; empty
! (get-type (+ 1 b)) ; Number
! (+ 1 b) ; no error, not reduced
! (+ 1 a) ; type error
```

In this program, we also tried to see the type of application of the grounded function to the argument of `%Undefined%` type. Such the expression type-checks. However, it is not reduced in the course of evaluation. Thus, grounded functions work as partial functions or expression constructors in such cases. MeTTa is a symbolic language, and the possibility to construct expressions for further analysis is one of its main features. Ultimately, grounded functions should not differ from symbolically defined functions in this regard.