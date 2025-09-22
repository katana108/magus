# Operations over atoms

Stdlib contains operations to construct and deconstruct atoms as instances of `Expression` meta-type. Let us first describe these operations.

## Deconstructing expressions

`car-atom` and `cdr-atom` are fundamental operations that are used to manipulate atoms. They are named after 'car' and 'cdr' operations in Lisp and other similar programming languages.

The `car-atom` function extracts the first atom of an expression as a tuple.

```
! (get-type car-atom) ; (-> Expression %Undefined%)
! (car-atom (1 2 3)) ; 1
! (car-atom (Cons X Nil)) ; Cons
! (car-atom (seg (point 1 1) (point 1 4))) ; seg
```

The `cdr-atom` function extracts the tail of an expression, that is, all the atoms of the argument except the first one.

```
! (get-type cdr-atom) ; (-> Expression %Undefined%)
! (cdr-atom (1 2 3)) ; (2 3)
! (cdr-atom (Cons X Nil)) ; (X Nil)
! (cdr-atom (seg (point 1 1) (point 1 4))) ; ((point 1 1) (point 1 4))
```

## Constructing expressions

`cons-atom` is a function, which constructs an expression using two arguments, the first of which serves as a head and the second serves as a tail.

```
! (get-type cons-atom) ; (-> Atom Expression Expression)
! (cons-atom 1 (2 3)) ; (1 2 3)
! (cons-atom Cons (X Nil)) ; (Cons X Nil)
! (cons-atom seg ((point 1 1) (point 1 4))) ; (seg (point 1 1) (point 1 4))
```

`cons-atom` reverses the results of `car-atom` and `cdr-atom`:

```
(= (reconstruct $xs)
   (let* (($head (car-atom $xs))
          ($tail (cdr-atom $xs)))
     (cons-atom $head $tail))
)
! (reconstruct (1 2 3)) ; (1 2 3)
! (reconstruct (Cons X Nil)) ; (Cons X Nil)
```

Note that we need `let` in the code above, because `cons-atom` expects "meta-typed" arguments, which are not reduced. For example, `cdr-atom` will not be evaluated in the following code:

```
! (cons-atom 1 (cdr-atom (1 2 3))) ; (1 cdr-atom (1 2 3))
```

Let us consider how basic recursive processing of expressions can be implemented:

```
(: map-expr (-> (-> $t $t) Expression Expression))
(= (map-expr $f $expr)
   (if (== $expr ()) ()
       (let* (($head (car-atom $expr))
              ($tail (cdr-atom $expr))
              ($head-new ($f $head))
              ($tail-new (map-expr $f $tail))
             )
         (cons-atom $head-new $tail-new)
       )
   )
)
! (map-expr not (False True False False))
```

## Comparison with custom data constructors

A typical way to construct lists using custom data structures is to introduce a symbol, which can be used for pattern-matching. Then, extracting heads and tails of lists becomes straightforward, and special functions for this are not need. They can be easily implemented via pattern-matching:

```
(= (car (Cons $x $xs)) $x)
(= (cdr (Cons $x $xs)) $xs)
! (cdr (Cons 1 (Cons 2 (Cons 3 Nil))))
```

But one can implement recursive processing without `car` and `cons`:

```
(: map (-> (-> $t $t) Expression Expression))
(= (map $f Nil) Nil)
(= (map $f (Cons $x $xs))
   (Cons ($f $x) (map $f $xs)))
! (map not (Cons False (Cons True (Cons False (Cons False Nil)))))
```

Instead of `Expression`, one would typically use a polymorphic `List` type (as described another tutorial).

Implementing `map` with the use of pattern matching over list constructors is much simpler. Why can't it be made with `cons-atom`? `cons-atom`, `car-atom`, `cdr-atom` work on the very base meta-level as grounded functions. If we introduced explicit constructors for expressions, then we would just move this meta-level further, and the question would arise how expressions with these new constructors are constructed. Apparently, we need to stop somewhere and introduce the very basic operations to construct all other composite expressions. Using explicit data constructors should typically be preferred over resorting to these atom-level operations.

## Typical usage

`car-atom` and `cdr-atom` are typically used for recursive traversal of an expression. One basic example is creation of lists from tuples. In case of reducible non-nested lists, the code is simple:

```
(= (to-list $expr)
   (if (== $expr ()) Nil
     (Cons (car-atom $expr)
           (to-list (cdr-atom $expr)))
   )
)
! (to-list (False (True False) False False))
```

Parsing a tuple of arbitrary length (if the use of explicit constructors is not convenient) is a good use case for operations with expressions. For example, one may try implementing `let*` by subsequently processing the tuple of variable-value pairs and applying `let`.

One more fundamental use case for analyzing expressions is implementation of custom interpretation schemes, if they go beyond the default MeTTa interpretation process and domain specific languages. A separate tutorial will be devoted to this topic. But let us note here that combining `car-atom` and `cdr-atom` with `get-metatype` will be a typical pattern here. Here, we provide a simple example for parsing nested tuples:

```
(= (to-tree $expr)
   (case (get-metatype $expr)
      ((Expression
         (if (== $expr ()) Nil
             (Cons (to-tree (car-atom $expr))
                   (to-tree (cdr-atom $expr)))
         ))
       ($_ $expr)
      )
   )
)
! (to-tree (False (True False) False False))
```

Note the difference of the result with `to-list`. The internal `(True False)` is also converted to the list now. It happens because the head of the current tuple is also passed to `to-tree`. For this to work, we need to analyze if the argument is an expression. If it is not, the value is not transformed.