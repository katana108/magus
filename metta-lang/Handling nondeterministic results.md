# Handling nondeterministic results

## Superpose

In previous tutorials we saw that `match` along with any other function can return multiple (nondeterministic) as well as empty results. If you need to get a nondeterministic result explicitly, use the `superpose` function, which turns a tuple into a nondeterministic result. It is an stdlib function of `(-> Expression Atom)` type.

However, it is typically recommended to avoid using it. For example, in the following program

```
(= (bin) 0)
(= (bin) 1)
(= (bin2) (superpose (0 1)))
! (bin) ; [0, 1]
! (bin2) ; [0, 1]
```

`bin` and `bin2` do similar job. However, `bin` is evaluated using one equality query, while `bin2` requires additional evaluation of `superpose`. Also, one may argue that `bin` is more modular and more suitable for meta-programming and evaluation control.

One may want to use `superpose` to execute several operations. However, the order of execution is not guaranteed. And again, one can try thinking about writing multiple equalities for a function, inside which `superpose` seems to be suitable.

However, `superpose` can still be convenient in some cases. For example, one can pass nondeterministic expressions to any function (both grounded and symbolic, built-in and custom) and get multiple results. In the following example, writing a nondeterministic function returning `3`, `4`, `5` would be inconvenient:

```
! (+ 2 (superpose (3 4 5))) ; [5, 6, 7]
```

Here, nondeterminism works like a map over a set of elements.

Another example, where using `superpose` explicitly is useful is for checking a set of nondeterministic results with `assertEqual`, when both arguments still require evaluation (so `assertEqualToResult` is not convenient to apply). In the following example, we want to check that we didn't forget any equality for `(color)`, but we may not be interested what exact value they are reduced to (i.e., whether `(ikb)` is reduced to `international-klein-blue` or something else).

```
(= (ikb) international-klein-blue)
(= (color) green)
(= (color) yellow)
(= (color) (ikb))

!(assertEqual
  (match &self (= (color) $x) $x)
  (superpose ((ikb) yellow green))) ; ()
!(assertEqualToResult
   (match &self (= (color) $x) $x)
  ((ikb) yellow green)) ; Error
```

## Empty

As mentioned above, in MeTTa, functions can return empty results. This is a natural consequence on the evaluation semantics based on queries, which can find no matches. Sometimes, we may want to force a function to "return" an empty result to abort a certain evaluation branch, or to explicitly represent it to analyze this behavior on the meta-level.

`(superpose ())` will exactly return the empty set of results. However, stdlib provide `(empty)` function to do the same in a clearer and stable way. Some versions may also use `Empty` as a symbol to inform the interpreter about the empty result, which may differ on some level from calling a grounded function, which really returns an empty set. `(empty)` is supported more widely at the moment, so we use it here.

`(empty)` could be useful in the construction of the asserts `(assertEqual (...) (empty))`, but `(assertEqualToResult (...) ())` can also work.

```
(Parent Bob Ann)
! (assertEqual
    (match &self (Parent Tom $x) $x)
    (empty)) ; ()
! (assertEqualToResult
    (match &self (Parent Tom $x) $x)
    ()) ; ()
```

Since expressions without suitable equalities remain unreduced in MeTTa, `(empty)` can be used to alter this behavior, when desirable, e.g.

```
(= (eq $x $x) True)
! (eq a b) ; (eq a b)
(= (eq $x $y) (empty))
! (eq a b) ; no result
```

`(empty)` can be used to turn a total function such as `if` or `unify` into a partial function, when we have no behavior for the else-branch, and we don't want the expression to remain unreduced.

Let us note that there is some convention in how the interpreter processes empty results. If the result of `match` for equality query is empty, the interpreter doesn't reduce the given expression (it transforms the empty result of such queries to `NotReducible`), but if a grounded function returns the empty result, it is treated as partial. When a grounded function application is not reduced, e.g. `(+ 1 undefined-symbol)`, because the function returns not the empty result, but `NotReducible`. This behavior may be refined in the future, but the possibility to have both types of behavior (a partial function is not reduced and evaluation continues or it returns no result stopping further evaluation) will be supported.

From nondeterministic viewpoint, `(empty)` removes an evaluation branch. If we consider all the results as a collection, `(empty)` can be used for its filtering. In the following program, `(color)` and `(fruit)` produce nondeterministic "collections" of colors and fruits correspondingly, while `filter-prefer` is a partially defined id function, which can be used to filter out these collections.

```
(= (color) red)
(= (color) green)
(= (color) blue)
(= (fruit) apple)
(= (fruit) banana)
(= (fruit) mango)
(= (filter-prefer blue) blue)
(= (filter-prefer banana) banana)
(= (filter-prefer mango) mango)
(= (filter-prefer $x) (empty))
! (filter-prefer (color)) ; [blue]
! (filter-prefer (fruit)) ; [mango, banana]
```

In case of recursion, `(empty)` can prune branches, which don't satisfy some conditions as shown in [this example](https://metta-lang.dev/docs/learn/tutorials/eval_intro/recursion_vars.html#solving-problems-with-recursive-nondeterminism).

## Collapse

Nondeterminism is an efficient way to map and filter sets of elements as well as to perform search. However, nondeterministic branches do not "see" each other, while we may want to get the extreme element or just to count them (or, more generally, fold over them). That is, we may need to collect the results in one evaluation branch.

Reverse operation to `superpose` is `collapse`, which has the type `(-> Atom Expression)`. It converts a nondeterministic result into a tuple.

`collapse` is a grounded function, which runs the interpreter on the given atom and wraps the returned results into an expression.

```
(= (color) red)
(= (color) green)
(= (color) blue)
! (color) ; three results: [blue, red, green]
! (collapse (color)) ; one result: [(blue red green)]
```

Here we've got a nondeterministic result `[blue, red, green]` from the `color` function and converted it into one tuple `[(blue red green)]` using `collapse`.

The `superpose` function reverts the `collapse` result

```
(= (color) green)
(= (color) yellow)
(= (color) red)
! (color) ; [green, yellow, red]
! (collapse (color)) ; [(green yellow red)]
! (let $x (collapse (color))
    (superpose $x))  ; [green, yellow, red]
! (superpose (1 2 3)) ; [1, 2, 3]
! (collapse (superpose (1 2 3)))
! (let $x (superpose (1 2 3)) ; [(1 2 3)]
    (collapse $x))    ; [(1), (2), (3)]
```

The color function gives the nondeterministic result `[green, yellow, red]` (the order of colors may vary). The `collapse` function converts it into a tuple `[(green yellow red)]`. And finally the `superpose` function in `let` converts a tuple back into the nondeterministic result `[red, green, yellow]`. The order of colors may change again due to nondeterminism.

Note that we cannot call `collapse` inside `superpose`, because `collapse` will not be executed before passing to `superpose` and will be considered as a part of the input tuple. In contrary, we cannot call `superpose` outside `collapse`, because it will cause `collapse` to be called separately for each nondeterministic branch produced by superpose instead of collecting these branches inside `collapse`.