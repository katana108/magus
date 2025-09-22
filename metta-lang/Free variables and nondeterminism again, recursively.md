# Free variables and nondeterminism again, recursively

## A piece of logic

We have already encountered `if`, which reduces to different expressions depending on whether its first argument is `True` or `False`. They are returned by such grounded operations as `>` or `==`. There are also such common logical operations as `and`, `or`, `not` in MeTTa (see the stdlib tutorial for more information). Things start to get interesting, when we pass free variables into logical expressions.

Let us consider the following program.

metta sandbox

There are some facts about `Fritz` and `Sam`, and there is a general rule about frogs. Just asking whether `(frog $x)` is `True`, we can infer that `Fritz` is a `Frog`, while `Sam` is not a `Frog` (detailed analysis of how it works is given in another tutorial).

`(green $x)` is defined in such a way that it is `True` when `(frog $x)` is `True`. However, if `(frog $x)` is `False`, it returns `(empty)` (which is evaluated to an empty set of results, which is equivalent to not defining a function on the corresponding data). Running the above code reveals that `Fritz` is green, but we cannot say whether `Sam` is green or not.

Make the replacement in the above code with the naive version of `(green $x)`.

```
(= (green $x)
   (if (frog $x) True (empty)))
(= (green $x) (frog $x))
```

This will result in `(Sam is-not Green)` to appear, which shows that `(= (green $x) (frog $x))` is not the same as logical implication even with boolean return values, although it is not precisely the same as equivalence (more on this in another tutorial).

You can also try to add `(= (eats_flies Tod) True)` into the set of facts. `(green Tod)` can be evaluated only partially (particular behavior is not fixed and might be different for different versions of MeTTa).

## Recursion with nondeterminism

Let us generalize generation of random binary pairs to binary lists of a given length. Examine the following program:

```
; random bit
(= (bin) 0)
(= (bin) 1)
; binary list
(= (gen-bin $n)
   (if (> $n 0)
       (:: (bin) (gen-bin (- $n 1)))
       ()))
! (gen-bin 3)
```

It will generate all the binary strings of length `3`. Similarly, functions to generate all the binary trees of the given depth, or all the strings up to a certain length can be written.

Try to write a function, which will output the binary list of the same length as an input list. You don't need to calculate the length of this list and to use `if`.

metta sandbox

## Solving problems with recursive nondeterminism

Let us put all the pieces together and solve the subset sum problem. In this problem, a list of integers is given, and one needs to find its elements whose sum will be equal to a given target sum. Candidate solutions in this problem can be represented as binary lists. Then, the sum of taken elements can be calculated as a sum of products of elements of two lists.

```
; random bit
(= (bin) 0)
(= (bin) 1)
; binary list with the same number of elements
(= (gen-bin-list ()) ())
(= (gen-bin-list (:: $x $xs))
   (:: (bin) (gen-bin-list $xs))
)
; sum of products of elements of two lists
(= (scalar-product () ()) 0)
(= (scalar-product (:: $x $xs) (:: $y $ys))
   (+ (* $x $y) (scalar-product $xs $ys))
)
; check the candidate solution
(= (test-solution $numbers $solution $target-sum)
   (if (== (scalar-product $numbers $solution)
           $target-sum)
       $solution
       (empty)
   )
)
; task
(= (task) (:: 8 (:: 3 (:: 10 (:: 17 ())))))
! (test-solution (task) (gen-bin-list (task)) 20)
```

This solution is not scalable, but it illustrates the general idea of how nondeterminism and recursion can be combined for problem solving. Note that passing a variable instead of `(gen-bin-list (task))` will not work here. What is the difference with the `frog` example? The answer will be given in the next tutorial.