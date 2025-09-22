## Recursive data types

All types allow constructing recursive expressions, when there is at least one function accepting and returning values of this type. This is true for arithmetic expressions or compositions of operations over strings. Say, any expression like `(+ (- 3 1) (* 2 (+ 3 4)))` will be of `Number` type. We expect that the result of evaluation of such expressions will have the same type as the reduced type of the expression itself.

However, in some cases, we don't even want such expressions to be reduced, but want to consider them as instances of the reduced type. Consider the simple example of Peano numbers:

```
(: Z Nat) ; Z is "zero"
(: S (-> Nat Nat)) ; S "constructs" the next number
! (S Z) ; this is "one"
! (S (S Z)) ; this is "two"
! (get-type (S (S (S Z)))) ; Nat
! (get-type (S S)) ; not Nat
```

We didn't define the type of `Nat` itself. One may prefer to add `(: Nat Type)` for clarity.

In the code above, `S` does nothing. It could be a grounded function, which adds `1` to the given number in some binary representation. Instead, `(S some-nat)` is not reduced and serves itself to represent the next natural number. It doesn't actually important that `S` is not a function, and `(S some-nat)` is not calculated. In fact, it could be. What really matters is that instances of `Nat` can be deconstructed and pattern-matched.

The following code shows, how `Nat` as a recursive data type is processed by pattern matching.

```
(: Z Nat)
(: S (-> Nat Nat))
(: Greater (-> Nat Nat Bool))
(= (Greater (S $x) Z)
   True)
(= (Greater Z $x)
   False)
(= (Greater (S $x) (S $y))
   (Greater $x $y))
! (Greater (S Z) (S Z)) ; False
! (Greater (S (S Z)) (S Z)) ; True
```

While this implementation is inefficient for computations, it is more suitable for reasoning.

More practical use of recursive data structures is in the form of containers to store data. We already constructed them in the previous tutorials, but without types. Let us add typing information and define the type of list of numbers:

```
(: NilNum ListNum)
(: ConsNum (-> Number ListNum ListNum))
! (get-type (ConsNum 1 (ConsNum 2 (ConsNum 3 NilNum)))) ; ListNum
! (ConsNum 1 (ConsNum "S" NilNum)) ; BadType
```

The type reduction for such expressions is rather straightforward: the type of `(ConsNum 3 NilNum)` is reduced to `ListNum`, since `ConsNum` is of `(-> Number ListNum ListNum)` type and its arguments are of `Number` and `ListNum` types. Consequently, `(ConsNum 2 (...))` is reduced to `ListNum` again for the same reason, and so on. For the second case, `(ConsNum "S" NilNum)` is badly typed.

Such expressions can be recursively processed as was done in the [tutorial](https://metta-lang.dev/docs/learn/tutorials/eval_intro/recursion.html). Adding type information makes the purpose of the corresponding functions clearer and allows detecting mistakes.

## Parametric types

Type expressions can contain variables. Type-checking for such types is implemented and can be understood via pattern-matching. Let us consider some basic examples.

Stdlib contains a comparison operator `==`. The following code

```
! (get-type ==)
! (== 1 "S")
```

will reveal that `(== 1 +)` is badly typed, and the reason is that `==` has the type `(-> $t $t Bool)`. This means that the arguments can be of an arbitrary but same type. Type-checking and reduction can be understood here as an attempt to unify `(-> $t $t Bool)` with `(-> Number String $result)`.

It deserves noting that the output type can also be variable, e.g.

```
(: apply (-> (-> $tx $ty) $tx $ty))
(= (apply $f $x) ($f $x))
! (apply not False) ; True
! (get-type (apply not False)) ; Bool
! (unify (-> (-> $tx  $ty)  $tx  $ty)
         (-> (-> Bool Bool) Bool $result)
         $result
         BadType) ; Bool
! (apply not 1) ; BadType
```

`not` has `(-> Bool Bool)` type and `False` is of `Bool` type. Thus, arguments of `(apply not False)` suppose that the function type signature should be unified with `(-> (-> Bool Bool) Bool $result)`. This results in binding both `$tx` and `$ty` to `Bool`, and the output type (`$ty`) also becomes `Bool`.

In the [tutorial](https://metta-lang.dev/docs/learn/tutorials/eval_intro/recursion.html), we defined `apply-twice`, which takes the function as an argument and applies it two time to the second argument. But what if the output type of the function is different from its input type? Can it be applied to the result of its own application? Try to specify the type of `apply-twice` to catch the error in the last expression:

metta sandbox

Besides defining higher-order functions, parametric types are useful for recursive data structures. One of the most common examples is `List`. How can we define it as a container of elements of an arbitrary but same type? We can parameterize the type `List` itself with the type of its elements:

```
(: Nil (List $t))
(: Cons (-> $t (List $t) (List $t)))
! (get-type (Cons 1 (Cons 2 Nil)))
! (get-type (Cons False (Cons True Nil)))
! (get-type (Cons + (Cons - Nil)))
! (get-type (Cons True (Cons 1 Nil)))
```

Let us consider how the type of `(Cons 2 Nil)` is derived. These arguments of `Cons` suppose its type signature to be undergo the following unification:

```
! (unify (-> $t     (List $t) (List $t))
         (-> Number (List $t) $result)
         $result
         BadType)
```

`$t` gets bound to `Number`, and the output type `(List $t)` becomes `(List Number)`.

Then, the outer `Cons` in `(Cons 1 (Cons 2 Nil))` receives the arguments of types `Number` and `(List Number)`, which can be simultaneously unified with `$t` and `(List $t)` producing `(List Number)` as the output type once again.

In contrast, the outer `Cons` in `(Cons True (Cons 1 Nil))` receives `Bool` and `(List Number)`. Apparently, `$t` in `(-> $t (List $t) (List $t))` cannot be bound to both `Bool` and `Number` resulting in type error.

Functions can receive arguments of parametric types, and type-checking will help to catch possible mistakes. Consider the following example

metta sandbox

We don't need function bodies for type-checking. `first` returns the first element of `(List $t)`-typed list, and this element should be of `$t` type. `append` concatenates two lists with elements of the same type and produces the list of elements of this type as well. When we start considering a specific expression and unify types of its elements with type signatures of corresponding functions, variables in types get bindings. Apparently, types of `(Cons 1 Nil)` and `(Cons 2 Nil)` are reduced to `(List Number)`. Then, `(append (...) (...))` gets the same type, while the type of `(first (...))` is reduced to `Number`. You can experiment with making the expression badly typed in the code above and see, at which point the error is detected.

Functional programming with types is discussed in more detail in [this tutorial](https://metta-lang.dev/docs/learn/tutorials/func_prog/intro.html). However, types in MeTTa are more general than generalized algebraic data types and are similar to dependent types. The use of such advanced types is elaborated in [this tutorial](https://metta-lang.dev/docs/learn/tutorials/types_adv/intro.html), in particular, in application to knowledge representation and reasoning.