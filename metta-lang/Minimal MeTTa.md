# Minimal MeTTa

Minimal MeTTa is a basic set of instructions, which are necessary and sufficient to implement the [MeTTa interpreter](https://github.com/trueagi-io/hyperon-experimental). The interpreter chains the [equality queries](https://metta-lang.dev/docs/learn/tutorials/ground_up/unify_func.html#function-evaluation-and-matching) and calls to grounded functions controlling this process depending on the current evaluation context and results including exceptions (errors), empty or non-reducible results. Thus, the main instruction in Minimal MeTTa is `eval`, which performs one step of evaluation, and which should be applied and chained explicitly. Any atom, which is not a Minimal MeTTa instruction (and not wrapped into such the instruction) will be evaluated to itself.

Minimal MeTTa instructions are available from MeTTa. However, their results can be different, because they will be processed by the MeTTa interpreter further. In order to work with pure Minimal MeTTa, one can use special `pragma`. If it is activated, the interpreter will not be used at all, and all expressions in the code will be evaluated without automatic chaining or additional processing. Consider the following example:

```
!(pragma! interpreter bare-minimal)
(= (foo) (bar))
(= (bar) a)
!(foo) ; (foo)
!(eval (foo)) ; (bar)
```

`(foo)` is not reduced, because `foo` is not a Minimal MeTTa instruction, while `(eval (foo))` is reduced, but only to `(bar)`, which is not automatically reduced further. Let us consider the basic Minimal MeTTa instructions.

## Basic operations: `chain`, `eval`, `unify`

### `eval`

`(eval ARG)` searches for the pattern `(= ARG $body)` in the current space and returns `$body` unified with the corresponding atom in the space if this equality pattern was matched or `NotReducible` symbol otherwise. Consider the following example

```
!(pragma! interpreter bare-minimal) ; ()
(= (foo) (bar))
(= (bar) a)
!(eval (foo)) ; (bar)
!(eval (bar)) ; a
!(baz) ; (baz)
!(eval (baz)) ; NotReducible
```

`(eval (foo))` is reduced to `(bar)` (but not to `a`), because `(= (foo) $body)` matches against `(= (foo) (bar))` with `$body` bound to `(bar)`, while `(eval (bar))` is reduced to `a`. In turn, `(eval (baz))` returns `NotReducible` symbol.

It should be noted that in MeTTa the type of `eval` is `(-> Atom Atom)`, so its result will not be evaluated further, but such special results as `NotReducible` will still be processed. Without `bare-minimal`, we'll get

```
(= (foo) (bar))
(= (bar) a)
!(baz) ; (baz)
!(eval (foo)) ; (bar)
!(eval (baz)) ; (eval (baz))
```

`(eval (baz))` in MeTTa remains itself, because it is `eval` that returns `NotReducible`, so the interpreter keeps the whole expression unreduced. Let us also emphasize that types are processed by the MeTTa interpreter (and could be processed in a different way), while the Minimal MeTTa instructions do not consider them.

It can be confusing at first that `(eval (baz))` produces different results in MeTTa and Minimal MeTTa, while `(baz)` remains itself in both cases. The latter has more complex reasons. `(baz)` is simply not evaluated in Minimal MeTTa, but the MeTTa interpreter tries to evaluate it (secretly calling `eval`), receives `NotReducible`, and returns `(baz)`, because it is `(baz)` that had no reduction rules (not `(eval (baz))` as in the previous example).

There are also other conditions and processing steps, which MeTTa interpreter is doing. Consider the following code:

```
(= A AA)
! A ; A
!(eval A) ; AA
```

The MeTTa interpreter applies `eval` only to expressions, which might be function applications. However, if one explicitly executes `eval` on a pure symbol, the equality query will also be constructed. There could be other choices, when to execute `eval` and how to deal with its results. Minimal MeTTa allows implementing different versions of the interpreter. Using Minimal MeTTa instructions from MeTTa can also be used to tweak the interpretation process. However, the fact should be taken into account that they will still be called not directly, but from the interpreter code.

We have covered only a part of `eval` functionality so far. If the argument is an expression, which first element is a grounded function, then `eval` calls this function and returns its result. If the result is a grounded error, it is converted as the following:

- `ExecError::Runtime` -> `(Error ...)`
- `ExecError::NoReduce` -> `NotReducible`
- `ExecError::IncorrectArgument` -> `NotReducible`

Let us note that even though `bare-minimal` turns the MeTTa interpreter off, Minimal MeTTa instructions are still called within its environment, so grounded functions from `stdlib` are available. Consider the following examples.

```
!(pragma! interpreter bare-minimal) ; ()
(= (foo) (bar))
(= (bar) a)
!(eval (match &self (= (foo) $x) $x)) ; (bar) 
!(eval (match &self (not-exist $x) $x)) ; Empty
!(eval (+ 1 2)) ; 3
!(eval (+ 1 "a")) ; NotReducible
!(eval (pow-math 2 200000000000000)) ; (Error (pow-math 2 200000000000000) power argument is too big, try using float value)
```

`match` is a grounded function, which can be executed via `eval`. If matching fails, the result is `Empty` in Minimal MeTTa. `+` or any other available grounded function can also be executed via `eval`. If the argument of a grounded function is not suitable, it will cause an error, which will be converted to `NotReducible` like in case of `(+ 1 "a")`. Other errors will be converted to an `Error`-expression.

It should be noted that `eval` doesn't process expressions recursively. If the top-level function is applicable to its arguments in their non-reduced form, then, it will be applied before the arguments reduction. Otherwise, the result will be `NotReducible`.

Consider the following example.

```
!(pragma! interpreter bare-minimal) ; ()
(= (foo $x) ($x $x))
(= (bar $x $y) ($y $x))
!(eval (bar (foo A) (foo B))) ; ((foo B) (foo A))
```

The result of `eval` is `((foo B) (foo A))` meaning that `bar` was successfully applied. Now, consider the following example

```
!(pragma! interpreter bare-minimal) ; ()
(= (foo OK) OK!!!)
(= (bar) OK)
!(eval (foo (bar))) ; NotReducible
!(eval ((bar))) ; NotReducible
!(eval (+ (+ 1 2) 3)) ; NotReducible
```

In all cases, there is no immediate way to evaluate the top-level function, even in the case of `((bar))` expression, which also requires peeking one level deeper into it. Thus, `eval` is a very basic instruction, and a lot of work is performed by the interpreter. Resorting to `eval` enables low-level control of the evaluation process, but a lot of functionality should be implemented on top of it manually.

## `unify`

`(unify ARG1 ARG2 UNIFIED NOT-UNIFIED)` tries to unify `ARG1` and `ARG2` atoms (any of which can contain variables) and returns `UNIFIED` (which typically but not necesserily contains variables from `ARG1` and/or `ARG2`) if unification is successful and returns `NOT-UNIFIED` otherwise.

The basic usage is as following:

```
!(pragma! interpreter bare-minimal) ; ()
!(unify (a $b) ($a b) ($a $b) fail) ; (a b)
!(unify (a $b) (b a) ok fail) ; fail
```

Wrapping `unify` into `eval` is not necessary even if `bare-minimal` is on, because it is a basic Minimal MeTTa instruction itself.

Since spaces implement custom matching, `unify` can accept them as one of its arguments. Thus, `unify` can be used instead of `match`, but with branching depending on the success of unification:

```
(friend Bob Alice)
!(unify &self (friend $who Alice) $who no-friends) ; Bob
!(unify &self (friend Pol $who) $who no-friends) ; no-friends
```

The latter can be achieved with `match` and `case` catching `Empty`, but in a less efficient way.

The code above works identically with and without `bare-minimal`. However, `unify` has `%Undefined%` return type in MeTTa, so its result will be evaluated further by the interpreter.

## `chain`

`eval` performs only one step of evaluation in Minimal MeTTa, and it is insufficient to perform chained evaluation of custom functions. For example, the following code returns `(bar)`.

```
!(pragma! interpreter bare-minimal) ; ()
(= (foo) (bar))
(= (bar) a)
!(eval (eval (foo))) ; (bar)
```

Why `(bar)` instead of `(eval (bar))` or `a`? Minimal MeTTa executes the outermost instruction. This is `eval`, which evaluates its argument. Since this argument is a grounded function call (inner `eval`), outer `eval` calls inner `eval` and it returns `(bar)`.

It should be underlined that the result of `eval` will not be evaluated by Minimal MeTTa even if it is a Minimal MeTTa instruction. There is no evaluation loop - just a set of instructions. The topmost instruction is executed in each expression in the program, and its **result** is not evaluated any further. Thus, **returned** `eval` will be the final result:

```
!(pragma! interpreter bare-minimal) ; ()
(= (foo) (eval (bar)))
(= (bar) a)
!(eval (foo)) ; (eval (bar))
```

A special instruction `(chain ARG $VAR RESULT)` in Minimal MeTTa is used to execute one instruction (`ARG`), bind `$VAR` (which should be a variable) to its result, and substitute `$VAR` inside `RESULT` which is returned after substitution:

```
!(pragma! interpreter bare-minimal)
!(eval (result is (+ 1 2))) ; NotReducible
!(chain (eval (+ 1 2)) $x (result is $x)) ; (result is 3)
!(eval (+ 1 (+ 2 3))) ; NotReducible
!(chain (eval (+ 2 3)) $x (eval (+ 1 $x))) ; 6
```

`chain` can be used to continue evaluation of a function, which returns `eval`:

```
!(pragma! interpreter bare-minimal) ; ()
(= (foo) (eval (bar)))
(= (bar) a)
!(chain (eval (foo)) $x $x) ; a
```

This example explicitly shows that `chain` not just returns its last argument (after substitution), but executes it in contrast to `eval`.

In Minimal MeTTa, arguments are always passed by `eval` to functions without changes, and subexpressions will never be evaluated. If one wants to construct a (possibly unreducible) expression by evaluating its subexpression, or to first evaluate a subexpression and then the whole expression, then it is necessary to use `chain` with this subexpression as `ARG` as shown in the example above. The MeTTa interpreter does this work - it traverses subexpressions and chains their evaluation keeping non-reducible (sub)expressions as is:

```
!(result is (+ 1 (+ 2 3))) ; (result is 6)
```

Let us consider a few more examples in Minimal MeTTa:

```
!(pragma! interpreter bare-minimal)
(= (foo) (bar))
(= (bar) a)
(= (buz $x) ($x $x))
!(chain (eval (foo)) $x (result is $x)) ; (result is (bar))
!(chain (eval (foo)) $x (eval $x)) ; a
!(chain (eval (foo)) $x (eval (buz $x))) ; ((bar) (bar))
!(chain (foo) $x (buz $x)) ; (buz (foo))
```

Apparently, if we perform only one step of evaluation of the function argument, this argument can remain not fully reduced. The only functionality provided by `chain` is to substitute the result of execution of one atom to another atom, and try to execute the result of substitution (which will be executed if it is a Minimal MeTTa instruction).

`chain` can be used in MeTTa instead of `let` if a Minimal MeTTa instruction (such as `eval` or `unify`) should be executed first. For example, `let` returns `Empty`, when the result of unification of its two arguments is empty, while `chain` still returns its last argument with substitutions, which may or may not be further reduced to `Empty`:

```
(= (id-eq $x $x) $x)
(= (id-eq $x $y) Empty)
!(let $r (id-eq 1 2) (quote $r)) ; []
!(let $r (eval (id-eq 1 2)) (quote $r)) ; []
!(chain (eval (id-eq 1 2)) $r (quote $r)) ; [(quote Empty)]
!(chain (eval (id-eq 1 2)) $r (it is $r)) ; []
```

`quote` has `Atom` as its argument type, so this argument is not evaluated. That is why `(quote Empty)` is a possible expression. However, in case of `let` this expression is simply not constructed. In case of `chain`, `(it is Empty)` is constructed but reduced to no result by the interpreter, because the whole tuple doesn't exist if one of its elements doesn't exist.

## Calculations in a loop: function/return

In principle, `eval`, `unify` and `chain` are enough to implement recursion with arbitrary depth, but it may require more `chain`s than expected:

```
!(pragma! interpreter bare-minimal)
(= (div $x $y $accum)
   (chain (eval (- $x $y)) $r1
     (chain (eval (< $r1 0)) $r2
       (chain (unify $r2 True
         $accum
         (chain (eval (+ 1 $accum)) $inc
           (chain (eval (div $r1 $y $inc)) $r4 $r4)
         )) $r3 $r3
       )
     )
   )
)
!(chain (eval (div 35 5 0)) $rr $rr) ; 7
```

We will not analyze this program in detail - just notice the number of `chain`s in it. Minimal MeTTa introduces a pair of instructions - `function` and `return`. `(function CODE)` evaluates `CODE` (and its result) until encounters `(return RESULT)`, after which it terminates and returns `RESULT`:

```
!(pragma! interpreter bare-minimal)
(= (foo) (eval (bar)))
(= (bar) (eval (baz)))
(= (baz) (return a))
(= (fooo) (function (eval (foo))))

!(function (eval (foo))) ; a
!(eval (fooo)) ; a
```

Let us consider the `div` example. With `function` and `return`, there will be two `chain`s less:

```
!(pragma! interpreter bare-minimal)
(= (div $x $y $accum)
   (chain (eval (- $x $y)) $r1
     (chain (eval (< $r1 0)) $r2
       (unify $r2 True
         (return $accum)
         (chain (eval (+ 1 $accum)) $inc
           (eval (div $r1 $y $inc))
         )
       )
     )
   )
)
!(function (eval (div 35 5 0))) ; 7
```

We still need to chain arithmetic calculations, so the profit seems not that big. However, the code looks more natural - we don't need to explicitly put the results of `unify` and `eval` inside `chain` and guess, how many additional steps of evaluation should be done.

`function` expects `(return RESULT)` expression, and if it encounters something else, which is not an executable Minimal MeTTa instruction, it return an error (`;` can be removed to see other error messages):

metta sandbox

In the last expression, `(eval (foo))` is evaluated by `function` until `(eval goo)` returns `G`, which is wrapped into `Error`.

An interesting feature of `function` is that it is treated by Minimal MeTTa in a special way. Unlike other instructions, it is executed even if it is a result of another instruction (not an argument of `eval` or `chain`). In the example below, `eval` and `chain` remain unreduced after being returned by `(eval (foo))` and `(eval (boo))` correspondingly, while `function` returned by `(eval (goo))` is evaluated:

```
!(pragma! interpreter bare-minimal)
(= (foo) (eval (+ 1 2)))
(= (boo) (chain (eval (+ 1 2)) $r $r))
(= (goo) (function (chain (eval (+ 1 2)) $r (return $r))))
! (eval (foo)) ; (eval (+ 1 2))
! (eval (boo)) ; (chain (eval (+ 1 2)) $r#nn $r#nn)
! (eval (goo)) ; 3
```

## `collapse-bind` and `superpose-bind`

`collapse-bind` and `superpose-bind` differ from collapse and superpose functions from `stdlib` in that they store not only atoms, but also bindings (values) of variables.

For example, `collapse-bind` can collect results of branches, in which the value of variable `$a` is different. `superpose-bind` applied to the result of `collapse-bind` will restore the value of this variable in each context. That's why `collapse-bind` returns and `superpose-bind` accepts not the list of atoms, but the list of pairs `(ATOM BINDING)`, where `BINDING` is a special grounded atom. In the following example, we have a nondeterministic function `xoo`. `collapse-bind` converts its results to a list of results with bindings.

```
!(pragma! interpreter bare-minimal)
(= (xoo a) xa)
(= (xoo b) xb)

!(chain
  (collapse-bind (eval (xoo $a))) $c
  ($c $a)) ; (((xb { $a <- b }) (xa { $a <- a })) $a)

!(chain
   (collapse-bind (eval (xoo $a))) $c
   (chain
     (superpose-bind $c) $x
     ($x $a))) ; [(xa a), (xb b)]
```

`chain` is used here to extract bindings of `$a` into the external context (i.e., to construct `($x $a)`).

`collapse-bind` is similar to `chain` in that it executes Minimal MeTTa instructions to collect the result.

## `cons-atom` and `decons-atom`

`cons-atom` constructs an expression given its head and tail, while `decons-atom` separates an expression into its head and tail, and returns them as a pair. `decons-atom` expects a non-empty expression.

```
!(cons-atom a (b c)) ; (a b c)
!(decons-atom (a b c)) ; (a (b c))
!(decons-atom (a)) ; (a ())
!(decons-atom ()) ; (Error (decons-atom ()) expected: (decons-atom (: <expr> Expression)), found: (decons-atom ()))
```