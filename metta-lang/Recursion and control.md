# Recursion and control

## Basic recursion

A natural way to represent repetitive computations in MeTTa is recursion like in traditional functional languages, especially for processing recursive data structures. Let us consider a very basic recursive function, which calculates the number of elements in the list.

```
(= (length ()) 0)
(= (length (:: $x $xs))
   (+ 1 (length $xs)))
! (length (:: A (:: B (:: C ()))))
```

The function has two cases, which are mutually exclusive de facto, and act as a conditional control structure. The base case returns `0` for an empty list `()`. Recursion itself takes place inside the second equality, in which `length` is defined via itself on the deconstructed parameter.

Notice that we didn't define the recursive data structure (list) here, and used arbitrary atoms (`::` and `()`) as data constructors. `length` can be called on anything, e.g. `(length (hello world))`, but this expression will simply be not reduced, because there are no suitable equalities for it. You can write your own version of length for other `Cons` and `Nil` instead of `::` and `()`:

metta sandbox

If a function expects specific subset of all possible expressions as input, types for corresponding atoms should be defined. However, we focus here on the basic evaluation process itself and leave types for [another tutorial](https://metta-lang.dev/docs/learn/tutorials/types_basics/parametric_types.html).

## Higher order functions

Higher-order functions is a powerful abstraction, which naturally appears in MeTTa. Consider the following code:

```
(= (apply-twice $f $x)
   ($f ($f $x)))
(= (square $x) (* $x $x))
(= (duplicate $x) ($x $x))
! (apply-twice square 2) ; 16
! (apply-twice duplicate 2) ; ((2 2) (2 2))
! (apply-twice 1 2) ; (1 (1 2))
```

`apply-twice` takes a function as its first parameter and applies it twice to its second parameter. In fact, it doesn't really care if it is a function or not. It simply constructs a corresponding expression for further evaluation.

Passing functions into recursive functions is very convenient for processing various collections. Consider the following basic example

```
(= (map $f ()) ())
(= (map $f (:: $x $xs))
   (:: ($f $x) (map $f $xs)))
(= (square $x) (* $x $x))
(= (twice $x) (* $x 2))
! (map square (:: 1 (:: 2 (:: 3 ())))) ; (:: 1 (:: 4 (:: 9 ())))
! (map twice (:: 1 (:: 2 (:: 3 ())))) ; (:: 2 (:: 4 (:: 6 ())))
! (map A (:: 1 (:: 2 (:: 3 ())))) ; (:: (A 1) (:: (A 2) (:: (A 3) ())))
```

`map` transforms a list by applying a given function (or constructor) to each element. There is a rich toolset of higher-order functions in functional programming. They are covered in [another tutorial](https://metta-lang.dev/docs/learn/tutorials/func_prog/intro.html).

## Conditional statements

Let us imagine that we want to implement the factorial operation. If we want to use grounded arithmetics, we will not be able to use pattern matching to deconstruct a grounded number and distinguish the base and recursive cases. We can write `(= (fact 0) 1)`, but we cannot just write `(= (fact $x) (* $x (fact (- $x 1))))`. However, we can use `if`, which works much like if-then-else construction in any other language. Consider the following code

```
(= (factorial $x)
   (if (> $x 0)
       (* $x (factorial (- $x 1)))
       1))
! (factorial 5) ; 120
```

`(factorial $x)` will be reduced to `(* $x (factorial (- $x 1)))` if `(> $x 0)` is `True`, and to `1` otherwise.

It should be noted that `if` doesn't evaluate all its arguments, but "then" and "else" branches are evaluated only when needed. `factorial` wouldn't work otherwise, although this should be more obvious from the following code, which will not execute the infinite loop

```
(= (loop) (loop)) ; this is an infinite loop 
! (if True Success (loop)) ; Success
```

Application of `if` looks like as an ordinary function application, and `if` is indeed implemented in pure MeTTa as a function. How it is done is discussed in [another tutorial](https://metta-lang.dev/docs/learn/tutorials/types_basics/metatypes.html#if-under-the-hood).

Another conditional statement in MeTTa is `case`, which pattern-matches the given atom against a number of patterns sequentially in a mutually exclusive way. A different version of the factorial operation can be implemented with it:

```
(= (factorial $x)
   (case $x
     ((0 1)
      ($_ (* $x (factorial (- $x 1)))))
   )
)
! (factorial 5) ; 120
```

In contrast to `if`, `case` doesn't check logical conditions but performs pattern matching similar to application of a function with several equality definitions. Thus, their usage is somewhat different. For example, if one wants to zip two lists, it is convenient to distinguish two cases - when both lists are empty, and both lists are not empty. But when two lists are of different lengths, there will a situation when neither of these cases will be applicable, and the expression will not be reduced. Try to run this code:

metta sandbox

The non-matchable part remains unreduced. Of course, adding two equalities for `(zip (:: $x $xs) ())` and `(zip () (:: $y $ys))` could be used (you can try to add them in the above code), and it would be a more preferable way in some cases. However, using `case` here could be more convenient:

```
(= (zip $list1 $list2)
   (case ($list1 $list2)
         (((() ()) ())
          (((:: $x $xs) (:: $y $ys)) (:: ($x $y) (zip $xs $ys)))
          ($else ERROR)
         )
   )
)
! (zip (:: A (:: B ())) (:: 1 (:: 2 ()))) ; (:: (A 1) (:: (B 2) ()))
! (zip (:: A (:: B ())) (:: 1 ())) ; (:: (A 1) ERROR)
```