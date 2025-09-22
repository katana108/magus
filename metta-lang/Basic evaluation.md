# Basic evaluation

## MeTTa programs

Programs in MeTTa consist of a number of atoms (mostly expressions, but individual symbols or grounded atoms can also be put there). A MeTTa script is a textual representation of the program, which is parsed atom-by-atom, and put into a program Space.

In particular, binary objects wrapped into grounded atoms are constructed from their textual representation in the course of parsing. For example, `+` and `1.05` will be turned into grounded atoms containing corresponding operation and value. Particular grounded atoms and their textual representation is not a part of the core MeTTa language, but is defined in modules (both built-in and custom). How modules and grounded atoms are introduced is discussed in another tutorial.

If a programmer wants some atom to be evaluated immediately instead of adding it to the Space, `!` should be put before it. The result of evaluation will not be added to the Space, but will be included into the output result of the whole program.

MeTTa scripts can also have comments, starting with `;`, which will be ignored by the parser.

In the following program, the first two atoms will be added to the program space, while the next two expressions will be immediately evaluated and appear in the output.

```
; This line will be ignored.
Hello ; This symbol will be added to the Space
(Hello World) ; This expression will also be added
! (+ 1 2) ; This expression will be immediatedly evaluated
! (Hi there) ; as well as this one
```

If an expression starts with a grounded atom containing an operation, this operation is executed on the other elements of the tuple acting as its arguments. `(+ 1 2)` is naturally evaluated to `3`.

At the same time, `(Hi there)` is evaluated to itself, because `Hi` is not a grounded operation, but just a custom symbol. It acts similar to a data constructor in Haskell (more on this in another tutorial). Let us consider how to do computations over symbolic expressions in MeTTa.

## Equalities

For a symbolic expression in MeTTa to be evaluated into something different from itself, an equality should be defined. Equality expressions work similar to function definitions in other languages. There is a number of important differences, though.

Let us consider a few examples.

- A nullary function simply returns its body

```
(= (h) (Hello world))
! (h)
```

- Some functions can accept only specific values of its argument. When this argument is passed, the right-hand side of the corresponding equality is returned

```
(= (only-a A) (Input A is accepted))
! (only-a A)
! (only-a B)
```

Note that `(only-a B)` is not reduced. In MeTTa, functions should not be total, and there is no hard boundary between a function and a data constructor. For example, consider this program:

```
! (respond me)
(= (respond me) (OK, I will respond))
! (respond me)
```

The first `(respond me)` will remain unchanged, while the second one will be transformed.

- Functions can have variables as parameters, just like in other languages.

```
(= (duplicate $x) ($x $x))
! (duplicate A)
! (duplicate 1.05)
```

The passed arguments replace corresponding variables in the right-hand part of the equality.

- Its arguments can be expressions with some structure

```
(= (swap (Pair $x $y)) (Pair $y $x))
! (swap (Pair A B)) ; evaluates to (Pair B A)
```

One may notice that this feature is similar to pattern matching in functional languages:

```
(= (Cdr (Cons $x $xs)) $xs)
! (Cdr (Cons A (Cons B Nil))) ; outputs (Cons B Nil)
```

But it is more general, because the structure of patterns can be arbitrary. In particular, patterns can contain the same variable encountered multiple times.

```
(= (check ($x $y $x)) ($x $y))
! (check (B A B)) ; reduced to (B A)
! (check (B A A)) ; not reduced
```

- Functions can have multiple (nondeterministic) results. The following code will output both `0` and `1`

```
(= (bin) 0)
(= (bin) 1)
! (bin) ; both 0 and 1
```

Note that equations for functions are not mutually exclusive, and the following code will output two results (not only `catched`) in the last case

```
(= (f special-value) catched)
(= (f $x) $x)
! (f A) ; A
! (f special-value) ; both catched and special-value
```

- Most importantly, variables can also be passed when calling a function, unlike imperative or functional languages. This will result in returning corresponding right-hand sides of equalities.

```
(= (brother Mike) Tom)
(= (brother Sam) Bob)
! (brother $x) ; just Tom and Bob are returned
! ((brother $x) is the brother of $x) ; the binding for $x is not lost
```

All these features are implemented using one mechanism, which is discussed later.

## Evaluation chaining

- The result of the function is evaluated further both for symbolic and grounded operation:

```
(= (square $x) (* $x $x))
! (square 3)
```

Here, `(square 3)` is first reduced to `(* 3 3)`, which, in turn, is evaluated to `9` by calling the grounded operation `*`.

In the following example, `Second` deconstructs the input list and returns `Car` for its tail, which is evaluated further

```
(= (Car (Cons $x $xs)) $x)
(= (Second (Cons $x $xs)) (Car $xs))
! (Second (Cons A (Cons B Nil))) ; outputs B
```

- Arguments of functions will typically be evaluated before the function is called. How this behavior can be controlled is discussed in a separate tutorial. The following examples should be pretty straightforward:

```
! (* (+ 1 2) (- 8 3)) ; 15
(= (square $x) (* $x $x))
! (square (+ 2 3)) ; 25
(= (triple $x) ($x $x $x))
(= (grid3x3 $x) (triple (triple $x)))
! (grid3x3 (square (+ 1 2))) ; ((9 9 9) (9 9 9) (9 9 9))
```

This behavior is not different from other, especially functional, languages.

- Passing results of nondeterministic functions to other functions (both deterministic and nondeterministic) cause the outer functions to be evaluated on each result. Consider the following examples:

```
; nondeterministic function
(= (bin) 0)
(= (bin) 1)
; deterministic triple
(= (triple $x) ($x $x $x))
! (triple (bin)) ; (0 0 0) and (1 1 1)
; nondeterministic pair
(= (bin2) ((bin) (bin)))
! (bin2) ; (0 0), (0 1), (1 0), (1 1)
; deterministic summation
(= (sum ($x $y)) (+ $x $y))
(= (sum ($x $y $z)) (+ $x (+ $y $z)))
! (sum (triple (bin))) ; 0, 3
! (sum (bin2)) ; 0, 1, 1, 2
; nondeterministic increment
(= (inc-flip $x) (+ 0 $x))
(= (inc-flip $x) (+ 1 $x))
! (inc-flip 1) ; 1, 2
! (inc-flip (bin)) ; 0, 1, 1, 2
```

`(triple (bin))` produces only two results, bevause `(bin)` is evaluated first and then passed to `triple`, while `(bin2)` produces four results, because each `(bin)` in its body is evaluated independently. Deterministic `sum` simply processes each nondeterministic value of its argument, while `inc-flip` doubles the number of input values.