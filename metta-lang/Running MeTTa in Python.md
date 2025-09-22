Running MeTTa in Python
Introduction

As Python has a broad range of applications, including web development, scientific and numeric computing, and especially AI, ML, and data analysis, its combined use with MeTTa significantly expands the possibilities of building AI systems. Both ways can be of interest:

    embedding Python objects into MeTTa for serving as sub-symbolic (and, in particular, neural) components within a symbolic system;
    using MeTTa from Python for defining knowledge, rules, functions, and variables which can be referred to in Python programs to create prompt templates for LLMs, logical reasoning, or compositions of multiple AI agents.

We start with the use of MeTTa from Python via high-level API, and then we will proceed to a tighter integration.
Setup

Firstly, you need to have MeTTa’s Python API installed as a Python package. MeTTa itself can be built from source with Python support and installed in the development mode in accordance with the instructions in the github repository. This approach is more involved, but it will yield the latest version with a number of configuration options.

However, for a quick start, hyperon package available via pip under Linux or MacOs (possibly except for newest processors):

pip install hyperon

MeTTa runner class

The main interface class for MeTTa in Python is MeTTa class, which represents a runner built on top of the interpreter to execute MeTTa programs. It can be imported from hyperon package and its instance can be created and used to run MeTTa code directly:

from hyperon import MeTTa
metta = MeTTa()
result = metta.run('''
   (= (foo) boo)
   ! (foo)
   ! (match &self (= ($f) boo) $f)
''')
print(result) # [[boo], [foo]]

The result of run is a list of results of all evaluated expressions (following the exclamation mark !). Each of this results is also a list (each containing one element in the example above). These results are not printed to the console by metta.run. They are just returned. Thus, we print them in Python.

Let us note that MeTTa instance preserve their program space after run has finished. Thus, run can be executed multiple times:

from hyperon import MeTTa
metta = MeTTa()
metta.run('''
	(Parent Tom Bob)
	(Parent Pam Bob)
	(Parent Tom Liz)
	(Parent Bob Ann)
''')
print(metta.run('!(match &self (Parent Tom $x) $x)')) # [[Liz, Bob]]
print(metta.run('!(match &self (Parent $x Bob) $x)')) # [[Tom, Pam]]

Parsing MeTTa code

The runner has methods for parsing a program code instead of executing it. Parsing produces MeTTa atoms wrapped into Python objects (so they can be manipulated from Python). Creating a simple expression atom (A B) looks like

atom = metta.parse_single('(A B)')

The parse_single() method parses only the next single token from the text program, thus the following example will give equivalent results

from hyperon import MeTTa
metta = MeTTa()
atom1 = metta.parse_single('(A B)')
atom2 = metta.parse_single('(A B) (C D)')
print(atom1) # (A B)
print(atom2) # (A B)

The parse_all() method can be used to parse the whole program code given in the string and get the list of atoms

from hyperon import MeTTa
metta = MeTTa()
program = metta.parse_all('(A B) (C D)')
print(program) # [(A B), (C D)]

Accessing the program Space

Let us recall that Atomspace (or just Space) is a key component of MeTTa. It is essentially a knowledge representation database (which can be thought of as a metagraph) and the associated MeTTa functions are used for storing and manipulating information.

One can get a reference to the current program Space, which in turn may be accessed directly, wrapped in some way, or passed to the MeTTa interpreter. Having the reference, one can add new atoms into it using the add_atom() method

metta.space().add_atom(atom)

Now let us call the run() method that runs the code from the program string containing a symbolic expression

from hyperon import MeTTa
metta = MeTTa()
atom = metta.parse_single('(A B)')
metta.space().add_atom(atom)
print(metta.run("!(match &self (A $x) $x)")) # [[B]]

The program passed to run contains only one expression !(match &self (A $x) $x). It calls the match function for the pattern (A $x) and returns all matches for the $x variable. The result will be [[B]], which means that add_atom has added (A B) expression extracted from the string by parse_single. The code

atom = metta.parse_single('(A B)')
metta.space().add_atom(atom)

is effectively equivalent to

metta.run('(A B)')

because expressions are not preceded by ! are just added to the program Space.

Please note that

atom = metta.parse_all('(A B)')

is not precisely equivalent to

metta.run('! (A B)')[0]

Although the results can be identical, the expression passed to run will be evaluated and can get reduced:

from hyperon import MeTTa
metta = MeTTa()
print(metta.run('! (A B)')[0])    # [(A B)]
print(metta.run('! (+ 1 2)')[0])  # [3]
print(metta.parse_all('(A B)'))   # [(A B)]
print(metta.parse_all('(+ 1 2)')) # [(+ 1 2)]

parse_single or parse_all are more useful, when we want not to add atoms to the program Space, but when we want to get these atoms without reduction and to process them further in Python.

Besides add_atom (and remove_atom as well), Space objects have query method.

metta = MeTTa()
metta.run('''
	(Parent Tom Bob)
	(Parent Pam Bob)
	(Parent Tom Liz)
	(Parent Bob Ann)
''')
pattern = metta.parse_single('(Parent $x Bob)')
print(metta.space().query(pattern)) # [{ $x <- Pam }, { $x <- Tom }]

In contrast to match in MeTTa itself, query doesn't take the output pattern, but just returns options for variable bindings, which can be useful for further custom processing in Python. It would be useful to have a possibility to define patterns directly in Python instead of parsing them from strings.
MeTTa atoms in Python

Class Atom in Python (see its implementation) is used to wrap all atoms created in the backend of MeTTa into Python objects, so they can be manipulated in Python. An atom of any kind (metatype) can be created as an instance of this class, but classes SymbolAtom, VariableAtom, ExpressionAtom and GroundedAtom together with helper functions are inherited from Atom for convenience.
SymbolAtom

Symbol atoms are intended for representing both procedural and declarative knowledge entities for fully introspective processing. Such symbolic representations can be used and manipulated to infer new knowledge, make decisions, and learn from experience. It's a way of handling and processing abstract and arbitrary information.

The helper function S() is a convenient tool to construct an instance of SymbolAtom Python class. Its only specific method is get_name, since symbols are identified by their names. All instances of Atom has get_metatype method, which returns the atom metatype maintained by the backend.

from hyperon import S, SymbolAtom, Atom
symbol_atom = S('MyAtom')
print(symbol_atom.get_name()) # MyAtom
print(symbol_atom.get_metatype()) # AtomKind.SYMBOL
print(type(symbol_atom)) # SymbolAtom
print(isinstance(symbol_atom, SymbolAtom)) # True
print(isinstance(symbol_atom, Atom)) # True

Let us note that S('MyAtom') is a direct way to construct a symbol atom without calling the parser as in metta.parse_single('MyAtom'). It allows constructing symbols with the use of arbitrary characters, which can be not accepted by the parser.
VariableAtom

A VariableAtom represents a variable (typically in an expression). It serves as a placeholder that can be matched with, or bound to other Atoms. V() is a convenient method to construct a VariableAtom:

from hyperon import V
var_atom = V('x')
print(var_atom) # $x
print(var_atom.get_name()) # x
print(var_atom.get_metatype()) # AtomKind.VARIABLE
print(type(var_atom)) # VariableAtom

VariableAtom also has get_name method. Please note that variable names don't include $ prefix in internal representation. It is used in the program code for the parser to distinguish variables and symbols.
ExpressionAtom

An ExpressionAtom is a list of Atoms of any kind, including expressions. It has the get_children() method that returns a list of all children Atoms of an expression. E() is a convenient method to construct expressions, it takes a list of atoms as an input. The example below shows that queries can be constructed in Python and the resulting expressions can be processed in Python as well.

from hyperon import E, S, V, MeTTa

metta = MeTTa()
expr_atom = E(S('Parent'), V('x'), S('Bob'))
print(expr_atom) # (Parent $x Bob)
print(expr_atom.get_metatype()) # AtomKind.EXPR
print(expr_atom.get_children()) # [Parent, $x, Bob]
# Let us use expr_atom in the query
metta = MeTTa()
metta.run('''
	(Parent Tom Bob)
	(Parent Pam Bob)
	(Parent Tom Liz)
	(Parent Bob Ann)
''')
print(metta.space().query(expr_atom)) # [{ $x <- Pam }, { $x <- Tom }]
result = metta.run('! (match &self (Parent $x Bob) (Retrieved $x))')[0]
print(result) # [(Retrieved Tom) (Retrieved Pam)]
# Ignore 'Retrieved' in expressions and print Pam, Tom
for r in result:
	print(r.get_children()[1])

GroundedAtom

GroundedAtom is a special subtype of Atom that makes a connection between the abstract, symbolically represented knowledge within AtomSpace and the external environment or the behaviors/actions in the outside world. Grounded Atoms often have an associated piece of program code that can be executed to produce specific output or trigger an action.

For example, this could be used to pull in data from external sources into the AtomSpace, to run a PyTorch model, to control an LLM agent, or to perform any other action that the system needs to interact with the external world, or just to perform intensive computations.

Besides the content, which a GroundedAtom wraps, there are three other aspects which can be customized:

    the type of GroundedAtom (kept within the Atom itself);
    the matching algorithm used by the Atom;
    a GroundedAtom can be made executable, and used to apply sub-symbolic operations to other Atoms as arguments.

Let us start with basic usage. G() is a convenient method to construct a GroundedAtom. It can accept any Python object, which has copy method. In the program below, we construct an expression with a custom grounded atom and add it to the program Space. Then, we perform querying to retrieve this atom. GroundedAtom has get_object() method to extract the data wrapped into the atom.

from hyperon import *
metta = MeTTa()
entry = E(S('my-key'), G({'a': 1, 'b': 2}))
metta.space().add_atom(entry)
result = metta.run('! (match &self (my-key $x) $x)')[0][0]
print(type(result)) # GroundedAtom
print(result.get_object()) # {'a': 1, 'b': 2}

As the example shows, we can add a custom grounded object to the space, query and get it in MeTTa, and retrieve back to Python.

However, wrapping Python object directly to G() is typically not recommended. Python API for MeTTa implements a generic class GroundedObject with the field content storing a Python object of interest and the copy method. There are two inherited classes, ValueObject and OperationObject with some additional functionality. Methods ValueAtom and OperationAtom is a sugared way to construct G(ValueObject(...)) and G(OperationObject(...)) correspondingly. Thus, it would be preferable to use ValueAtom({'a': 1, 'b': 2}) in the code above, although one would need to write result.get_object().content to access the corresponding Python object (ValueObject has a getter value for content as well, while OperationObject uses op for this).

The GroundedObject constructor takes a content argument (a Python object) to wrap into a grounded atom. It also optionally accepts an id argument to represent the atom and to compare atoms if using the content for this purpose isn't ideal. The ValueObject class provides a getter method value to return the content of the grounded atom.

Arguments of the OperationObject constructor include name, op, and unwrap. name serves as the id for the grounded atom, op (a function) defining the operation is used as the content of the grounded atom, and unwrap (a boolean, optional) indicates whether to unwrap the GroundedAtom content when applying the operation (see more on uwrap on the next page of this tutorial).

While there is a choice whether to use ValueAtom and OperationAtom classes for custom objects or to directly wrap them into G, grounded objects constructed in the MeTTa code are returned as such sugared atoms:

from hyperon import *
metta = MeTTa()
calc = metta.run('! (+ 1 2)')[0][0]
print(type(calc.get_object())) # ValueObject
print(calc.get_object().value) # 3

metta.run('(my-secret-symbol 42)') # add the expression to the space
pattern = E(V('x'), ValueAtom(42))
print(metta.space().query(pattern)) # { $x <- my-secret-symbol }

As can be seen from the example, ValueAtom(42) can be matched against 42 appeared in the MeTTa program (although it is not recommended to use grounded atoms as keys for querying).

It should be noted, however, that stdlib operations in MeTTa are not Python operations. While atoms wrapping objects of such privitive types as Number are automatically converted into Python objects (so one can get Python 3 from calculations !(+ 1 2) in MeTTa), the following code will cause a error, because the grounded operation wrapped by + atom is not a Python operation.

plus = metta.parse_single('+')
plus.get_object()

There is a module called py_ops, which replaces some basic operations with Python operations, so the following code works:

from hyperon import *
metta = MeTTa()
metta.run("! (import! &self py_ops)")
plus = metta.parse_single('+')
print(type(plus.get_object())) # OperationObject
print(plus.get_object().op) # some lambda
print(plus.get_object()) # + as a representation of this operation
print(metta.run('!(* "A" 4)')) # [["AAAA"]]

Apparently, there is a textual representation of grounded atoms, from which atoms themselves are built by the parser. But is it possible to introduce such textual representations for custom grounded atoms, so we could refer to them in the textual program code? The answer is yes. The Python and MeTTa API for this is described on the next page.