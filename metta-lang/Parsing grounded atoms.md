# Parsing grounded atoms

## Tokenizer

The MeTTa interpreter operates with the internal representation of programs in the form of atoms. Atoms can be constructed in the course of parsing or directly using the corresponding API. Let us examine what atoms are constructed by the parser. In the following program, we parse the expression `(+ 1 S)`.

```
from hyperon import *
metta = MeTTa()
expr1 = metta.parse_single('(+ 1 S)')
expr2 = E(S('+'), S('1'), S('S'))
print('Expr1: ', expr1)
print('Expr2: ', expr2)
print('Equal: ', expr1 == expr2)
for atom in expr1.get_children():
    print(f'type({atom})={type(atom)}')
```

The result of parsing differs from the expression `(+ 1 S)` composed of symbolic atoms. Indeed, the atoms constructed from `+` and `1` by the parser are grounded atoms - not symbols. At the same time, `S('+')` is already a symbol atom.

Transformation of the textual representation to grounded atoms is not hard-coded. It is done by the tokenizer on the base of a mapping from tokens in the form of regular expressions to constructors of corresponding grounded atoms.

The initial mapping is provided by the `stdlib` module, but it can be modified later. In the simple case, tokens are just strings. For example, the tokenizer is informed that if `+` is encountered in the course of parsing, the following atom should be constructed

```
OperationAtom('+', lambda a, b: a + b,
              ['Number', 'Number', 'Number'])
```

Here, `['Number', 'Number', 'Number']` is a sugared way to defined the type `(-> Number Number Numer)`, which should also be represented as an atom.

Regular expressions are needed for such cases as parsing numbers. For example, integers are constructed on the base of the token `r"[-+]?\d+"`, and the constructor needs to get the token itself, so the atom is created by the following function once the token is encountered

```
lambda token: ValueAtom(int(token), 'Number')
```

## `evaluate_atom`

Once atoms are created, the interpreter doesn't rely on the tokenizer. Instances of `MeTTa` class have method `evaluate_atom`, which is the function accepting the atom to interpret.

```
from hyperon import *
metta = MeTTa()
expr1 = metta.parse_single('(+ 1 2)')
print(metta.evaluate_atom(expr1))
expr2 = E(OperationAtom('+', lambda a, b: a + b),
          ValueAtom(1), ValueAtom(2))
print(metta.evaluate_atom(expr2))
```

The example above shows that the parsed expression is interpreted in the same ways as the expression atom constructed directly. `MeTTa.run` simply parses the program code expression-by-expression and puts the resulting atoms in the program space or immediately interprets them when `!` precedes the expression. Note that we could get the operation atom for `+` (which would be correctly typed) via `metta.parse_single('+')`

## Creating new tokens

Access to the tokenizer is provided by the `tokenizer()` method of the `MeTTa` class. However, it may not be used directly. `MeTTa` class has the `register_token` method, which is intended for registering a new token. It accepts a regular expression and a function, which will be called to construct an atom each time the token is encountered. The constructed atom should not necessarily be a grounded atom, although it is the most typical case.

If the token is a mere string, and creation of different atoms depending on a regular expression is not supposed, `register_atom` can be used. It accepts a regular expression and an atom, and calls `register_token` with the given token and with the lambda simply returning the given atom.

The following example illustrates creation of an Atomspace and wrapping it into a `GroundedAtom`

```
from hyperon import *

metta = MeTTa()

# Getting a reference to a native GroundingSpace,
# implemented by the MeTTa core library.
grounding_space = GroundingSpaceRef()
grounding_space.add_atom(E(S("A"), S("B")))
space_atom = G(grounding_space)

# Registering a new custom token based on a regular expression.
# The new token can be used in a MeTTa program.
metta.register_atom("&space", space_atom)
print(metta.run("! (match &space (A $x) $x)"))
```

## Parsing and interpretation

Although the interpreter works with the representation of programs in the form of atoms (as was mentioned above), and expressions should be parsed before being interpreted, the tokenizer can be changed in the course of MeTTa script execution. It is essential for the MeTTa module system (described in more detail in another tutorial).

[`import!`](https://metta-lang.dev/docs/learn/tutorials/stdlib_overview/working_with_spaces.html#imports) is not only loads a module code into a space. It can also modify the tokenizer with tokens declared in the module. This is the reason why a MeTTa is not first entirely converted to atoms and then interpreted, but parsing and interpretation are intervened. Another approach would be to load all the atoms as symbols and resolve them at runtime, so the interpreter would verify if some symbols are grounded in subsymbolic data. This approach would have its benefits, and it might be chosen in the future versions of MeTTa. However, it would imply that introduction of new groundings to symbols has retrospective effect on the previous code.

We have also encountered creation of new tokens inside MeTTa programs with the use of [`bind!`](https://metta-lang.dev/docs/learn/tutorials/stdlib_overview/working_with_spaces.html#creating-tokens) showing that token bindings don't have backward effect. The same is definitely true, when we create tokens using Python API:

```
from hyperon import *

# A function to be registered
def dup_str(s, n):
    r = ""
    for i in range(n):
        r += s
    return r

metta = MeTTa()
# Create an atom. "dup-str" is its internal name
dup_str_atom = OperationAtom("dup-str", dup_str)

# Interpreter will call this operation atom provided directly
print(metta.evaluate_atom(E(dup_str_atom, ValueAtom("-hello-"), ValueAtom(3))))

# Let us add a function calling `dup-str`
metta.run('''
  (= (test-dup-str) (dup-str "a" 2))
''')

# The parser doesn't know it, so dup-str will not be reduced
print(metta.run('''
 ! (dup-str "-hello-" 3)
 ! (test-dup-str)
'''))

# Now the token is registered. New expression will be reduced.
# However, `(= (test-dup-str) (dup-str "a" 2))` was added
# before `dup-str` token was introduced. Thus, it will still
# remain not reduced.
metta.register_atom("dup-str", dup_str_atom)
print(metta.run('''
! (dup-str "-hello-" 3)
! (test-dup-str)
'''))
```

## Kwargs for OperationAtom

Python supports variable number of arguments in functions. Such functions can be wrapped into grounded atoms as well.

```
from hyperon import *
def print_all(*args):
    for a in args:
        print(a)
    return [Atoms.UNIT]
metta = MeTTa()
metta.register_atom("print-all", OperationAtom("print-all", print_all))
metta.run('(print-all "Hello" (+ 40 2) "World")')
```

In cases when the function representing the operation has optional arguments with default values, the `Kwargs` keyword can be used to pass the keyword parameters. For example, let us define a grounded function `find-pos` which receives two strings and searches for the position of the second string in the first one. Let the default value for the second string be `"a"`. Additionally, this function has the third parameter which specifies whether the search should start from the left or the right, with the default value being `left=True`.

```
from hyperon import *
def find_pos(x:str, y="a", left=True):
    if left:
        return x.find(y)
    pos = x[-1:].find(y)
    return len(x) - 1 - pos if pos >= 0 else pos
metta = MeTTa()
metta.register_atom("find-pos", OperationAtom("find-pos", find_pos))
print(metta.run('''
 ! (find-pos "alpha") ; 0
 ! (find-pos (Kwargs (x "alpha") (left False))) ; 4
 ! (find-pos (Kwargs (x "alpha") (y "c") (left False))) ; -1
'''))
```

Hence, to set argument values using Kwargs, one needs to pass pairs of argument names and values.

## Unwrapping Python objects from atoms

Above, we have introduced a summation operation as `OperationAtom('+', lambda a, b: a + b)`,where `a` and `b` are Python numbers instead of atoms. `a + b` is also not an atom. Creating of operation atoms getting Python objects is convenient, because it eliminates the necessity to retrieve values from grounded atoms and wrap the result of the operation back to the grounded atom. However, sometimes it is needed to write functions that operate with atoms themselves, and these atoms may not be grounded atoms wrapping Python objects.

Unwrapping Python values from input atoms and wrapping the result back into a grounded atom is the default behavior of `OperationAtom`, which is controlled by the parameter `unwrap`. Let us consider an example of implementing `+` while setting this parameter to `False`.

```
def plus(atom1, atom2):
    from hyperon import ValueAtom
    sum = atom1.get_object().value + atom2.get_object().value
    return [ValueAtom(sum, 'Number')]

from hyperon import OperationAtom, MeTTa
plus_atom = OperationAtom("plus", plus,
    ['Number', 'Number', 'Number'], unwrap=False)
metta = MeTTa()
metta.register_atom("plus", plus_atom)
print(metta.run('! (plus 3 5)'))
```

When `unwrap` is `False`, a function should be aware of the `hyperon` module, which can be inconvenient for purely Python functions. Thus, this setting is desirable for functions processing or creating atoms themselves. For example, `bind!` takes an atom to be bound to a token. `parse` takes a string and return an atom of any metatype constructed by parsing this string. One can imagine different custom operations, which accept and return atoms. Say, if a crossover operation in genetic algorithms would be implemented as a grounded operation, it would accept two atoms (typically, expressions), traverse them to find crossover points, and construct a child expression.