# Working with spaces

## Space API

Spaces can have different implementations, but should satisfy a certain API. This API includes pattern-matching (or unification) functionality. `match` is an stdlib function, which calls a corresponding API function of the given space, which can be different from the program space.

Let us recap that the type of `match` is `(-> hyperon::space::DynSpace Atom Atom %Undefined%)`. The first argument is a space (or, more precisely, a grounded atom referring to a space) satisfying the Space API. The second argument is the input pattern to be unified with expressions in the space, and the third argument is the output pattern, which is instantiated for every found match. `match` can produce any number of results starting with zero, which are treated nondeterministically.

The basic use of `match` was already covered before, while its use with custom spaces will be described in other tutorials, since these spaces are not the part of stdlib. However, the Space API includes additional components, which are utilized by such stdlib functions as `add-atom` and `remove-atom`.

## Adding atoms

The content of spaces can be not only defined statically in MeTTa scripts, but can also be modified at runtime by programs residing in the same or other spaces.

The function `add-atom` adds an atom into the Space. Its type is `(-> hyperon::space::DynSpace Atom (->))`. The first argument is an atom referring some Space, to which an atom provided as the second argument will be added. Since the type of the second argument is `Atom`, the added atom is added as is without reduction.

In the following program, `add-foo-eq` is a function, which adds an equality for `foo` to the program space whenever called. Then, it is checked that the expressions are added to the space without reduction.

```
(: add-foo-eq (-> Atom (->)))
(= (add-foo-eq $x)
   (add-atom &self (= (foo) $x)))
! (foo) ; (foo) - not reduced
! (add-foo-eq (+ 1 2)) ; () - OK
! (add-foo-eq (+ 3 4)) ; () - OK
! (foo) ; [3, 7]
! (match &self (= (foo) $x)
    (quote $x)) ; [(quote (+ 1 2)), (quote (+ 3 4))]
```

If it is desirable to add a reduced atom without additional wrappers (e.g., like `add-foo-eq` but without `Atom` type for the argument), then `add-reduct` can be used:

```
! (add-reduct &self (= (foo) (+ 3 4))) ; ()
! (foo) ; 7
! (match &self (= (foo) $x)
    (quote $x)) ; (quote 7)
```

## Removing atoms

The function `remove-atom` removes an atom from the AtomSpace without reducing it. Its type is `(-> hyperon::space::DynSpace Atom (->))`.

The first argument is a reference to the space from which the Atom needs to be removed, the second is the atom to be removed. Notice that if the given atom is not in the space, `remove-atom` currently neither raises a error nor returns the empty result.

```
(Atom to remove)
! (match &self (Atom to remove) "Atom exists") ; "Atom exists"
! (remove-atom &self (Atom to remove)) ; ()
! (match &self (Atom to remove) "Unexpected") ; nothing
! (remove-atom &self (Atom to remove)) ; ()
```

Combination of `remove-atom` and `add-atom` can be used for [graph rewriting](https://en.wikipedia.org/wiki/Graph_rewriting). Consider the following example.

```
(link A B)
(link B C)
(link C A)
(link C E)

! (match &self (, (link $x $y)
                  (link $y $z)
                  (link $z $x))
               (let () (remove-atom &self (link $x $y))
                       (add-atom &self (link $y $x)))
  ) ; [(), (), ()]
! (match &self (link $x $y)
    (link $x $y)) ; [(link A C), (link C B), (link B A), (link C E)]
```

Here, we find entries `(link _ _)`, which form three-element loops, and revert the direction of links in them. Let us note that `match` returns three unit results, because the loop can start from any of such entries. All of them are reverted (only `(link C E)` remains unchanged). Also, in the current implementation, `match` first finds all the matches, and then instantiates the output pattern with them, which is evaluated outside `match`. If `remove-atom` and `add-atom` would be executed right away for each found matching, the condition of circular links would be broken after the first rewrite. This behavior can be space-specific, and is not a part of MeTTa specification at the moment. This can be changed in the future.

## New spaces

It is possible to create other spaces with the use of `new-space` function from stdlib. Its type is `(-> hyperon::space::DynSpace)`, so it has no arguments and returns a fresh space. Creating new spaces can be useful to keep the program space cleaner, or to simplify queries.

If we just run `(new-space)` like this

```
! (new-space)
```

we will get something like `GroundingSpace-0x10703b398` as a textual representation space atom. But how can we refer to this space in other parts of the program? Notice that the following code will not work as desired

```
(= (get-space) (new-space))
! (add-atom (get-space) (Parent Bob Ann)) ; ()
! (match (get-space) (Parent $x $y) ($x $y)) ; nothing
```

because `(get-space)` will create a brand new space each time.

One workaround for this issue in a functional programming style is to wrap the whole program into a function, which accepts a space as an input and passes it to subfunctions, which need it:

```
(= (main $space)
   (let () (add-atom $space (Parent Bob Ann))
     (match $space (Parent $x $y) ($x $y))
   )
)
! (main (new-space)) ; (Bob Ann)
```

This approach has its own merits. However, a more direct fix for `(= (get-space) (new-space))` would be just to evaluate `(new-space)` before adding it to the program:

```
! (add-reduct &self (= (get-space) (new-space))) ; ()
! (add-atom (get-space) (Parent Bob Ann)) ; ()
! (get-space) ; GroundingSpace-addr
! (match (get-space) (Parent $x $y) ($x $y)) ; (Bob Ann)
```

That is, `(new-space)` is evaluated to a grounded atom, which wraps a newly created space. Other elements of `(= (get-space) (new-space))` are not reduced. Instead of `add-reduct`, one could use the following more explicit code

```
! (let $space (new-space)
    (add-atom &self (= (get-space) $space)))
```

which also ensured that nothing is reduced except `(new-space)`.

## Creating tokens

Why can't we refer to the grounded atom, which wraps the created space? Indeed, we can represent such grounded atoms as numbers or operations over them in the code. And what is about `&self`?

In fact, they are turned into atoms from their textual representation by the parser, which knows a mapping from textual tokens (defined with the use of regular expressions) to constructors of corresponding grounded atom. Basically, `&self` is replaced with the grounded atom wrapping the program space by the parser before it gets inside the interpreter.

Parsing is explained in more detail in [another tutorial](https://metta-lang.dev/docs/learn/tutorials/python_use/tokenizer.html), while here we focus on the stdlib function `bind!`.

`bind!` registers a new token which is replaced with an atom during the parsing of the rest of the program. Its type is `(-> Symbol %Undefined% (->))`.

The first argument has type `Symbol`, so technically we can use any valid symbol as the token name, but conventionally the token should start with `&`, when it is bound to a custom grounded atom, to distinguish it from symbols. The second argument is the atom, which is associated with the token after reduction. This atom should not necessarily be a grounded atom. `bind!` returns the unit value `()` similar to `println!` or `add-atom`.

Consider the following program:

```
(= (get-hello) &hello)
! (bind! &hello (Hello world)) ; ()
! (get-metatype &hello) ; Expression
! &hello ; (Hello world)
! (get-hello) ; &hello
```

We first define the function `(get-hello)`, which returns the symbol `&hello`. Then, we bind the token `&hello` to the atom `(Hello world)`. Note that the metatype of `&hello` is `Expression`, because it is replaced by the parser and gets to the interpreter already as `(Hello world)`. `! &hello` is expectedly `(Hello world)`. Once again, `&hello` is not reduced to `(Hello world)` by the interpreter. It is replaced with it by the parser. It can be seen by the fact that `(get-hello)` returns `&hello` as a symbol, because it was parsed and added to the program space before `bind!`.

`bind!` might be tempting to use to refer to some lengthy constant expressions, e.g.

```
! (bind! &x (foo1 (foo2 3) 45 (A (v))))
! &x
```

However, this lengthy expression will be inserted to the program in place of every occurrence of `&x`. However, let us note again that the second argument of `bind!` is evaluated before `bind!` is called, which is especially important with functions with side effects. For example, the following program will print `"test"` only once, while `&res` will be simply replaced with `()`.

```
! (bind! &res (println! "test"))
! &res
! &res
```

Using `bind!` for unique grounded atoms intensively used in the program can be more reasonable. Binding spaces created with `(new-space)` to tokens is one of possible use cases:

```
! (bind! &space (new-space)) ; ()
! (add-atom &space (Parent Bob Ann)) ; ()
! &space ; GroundingSpace-addr
! (match &space (Parent $x $y) ($x $y)) ; (Bob Ann)
! (match &self (Parent $x $y) ($x $y)) ; empty
```

However, if spaces are created dynamically depending on runtime data, `bind!` is not usable.

## Imports

Stdlib has operations for importing scripts and modules. One such operation is `import!`. It accepts two arguments. The first argument is a symbol, which is turned into the token for accessing the imported module. The second argument is the module name. For example, the program from the [tutorial](https://metta-lang.dev/docs/learn/tutorials/ground_up/nested_queries.html#composite-queries) could be split into two scripts - one containing knowledge, and another one querying it.

```
; people_kb.metta
(Female Pam)
(Male Tom)
(Male Bob)
(Female Liz)
(Female Pat)
(Female Ann)
(Male Jim)
(Parent Tom Bob)
(Parent Pam Bob)
(Parent Tom Liz)
(Parent Bob Ann)
(Parent Bob Pat)
(Parent Pat Jim)
```

```
; main.metta
! (import! &people people_kb)
(= (get-sister $x)
   (match &people
     (, (Parent $y $x)
        (Parent $y $z)
        (Female $z))
     $z
   )
)
! (get-sister Bob)
```

Here, `(import! &people people_kb)` looks similar to `(bind! &people (new-space))`, but `import!` fills in the loaded space with atoms from the script. Let us note that `import!` does more work than just loading the script into a space. It interacts with the module system, which is described in another tutorial.

`&self` can be passed as the first argument to `import!`. In this case, the script or module will still be loaded into a separate space, but the atom wrapping this space will be inserted to `&self`. Pattern matching queries encountering such atoms will delegate queries to them (with the exception, when the space atom itself matches against the query, which happens, when this query is just a variable, e.g., `$x`). Thus, it works similar to inserting all the atoms to `&self`, but with some differences, when importing the same module happens multiple times, say, in different submodules.

One may use `get-atoms` method to see that the empty MeTTa script is not that empty and contains the stdlib space(s). Note that the result `get-atoms` will be reduced. Thus, it is not recommended to use in general.

```
! (get-atoms &self)
```

Some space atoms are present in the seemingly empty program since some modules are pre-imported. Indeed, one can find, say, `if` definition in `&self`, which actually resides in the stdlib space inserted into `&self` as an atom

```
! (match &self
          (= (if $cond $then $else) $result)
   (quote (= (if $cond $then $else) $result))
  )
```

`mod-space!` returns the space of the module (and tries to load the module if it is not loaded into the module system). Thus, we can explore the module space explicitly.

```
! (mod-space! stdlib)
! (match (mod-space! stdlib)
          (= (if $cond $then $else) $result)
   (quote (= (if $cond $then $else) $result))
  )
```