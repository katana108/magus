# Main concepts

## Atoms and knowledge graphs

MeTTa (Meta Type Talk) is a multi-paradigm language for declarative and functional computations over knowledge (meta)graphs.

Every MeTTa program lives inside of a particular **Atomspace** (or just **Space** if we don't insist on a particular internal representation). Atomspace is a part of the [OpenCog (Hyperon)](https://wiki.opencog.org/w/Hyperon) software ecosystem and it is essentially a knowledge database with the associated query engine to fetch and manipulate that knowledge. MeTTa programs can contain both factual knowledge and rules or functional code to perform reasoning on knowledge including programs themselves making the language fully self-reflective. One can draw an analogy with Prolog, which programs can also be considered as a knowledge base content, but with less introspective and more restrictive representation.

In an Atomspace, an **Atom** is a fundamental building block of all the data. In the context of graph representation, an Atom can be either a node or a link. In an Atomspace as metagraph, links can connect not only nodes, but other links, that is, they connect atoms, and they can connect any number of atoms (in contrast to ordinary graphs). In MeTTa as a programming language, atoms play the role of terms.

In the context of AI, Atoms can represent anything from objects, to concepts, to processes, functions or relationships. This enables the creation of rich, complex models of knowledge and reasoning.

## Atom kinds and types

There are 4 kinds of Atoms in MeTTa:

- **Symbol**, which represents some idea or concept. Two symbols having the same name are considered equal and representing the same concept. Names of symbols can be arbitrary strings. Nearly anything can be a symbol, e.g., `A`, `f`, `known?`, `replace-me`, `≱`, etc.
- **Expression**, which can encapsulate other atoms including other expressions. Basic MeTTa syntax is Scheme-like, e.g. `(f A)`, `(implies (human Socrates) (mortal Socrates))`, etc.
- **Variable**, which is used to create patterns (expressions with variables). Such patterns can be matched against other atoms to assign some specific binding to their variables. Variables are syntactically distinguished by a leading `$`, e.g. `$x`, `$_`, `$my-argument`, which tells the parser to convert a symbol to a variable. Patterns could be `(Parent $x $y)`, `(Implies (Human $x) (Mortal $x))`, `(:- (And (Implies $x $y) (Fact $x)) $y)`, or any other symbolic expression with variables. Such patterns get meaning when they are matched against expressions in the Atomspace.
- **Grounded**, which represents sub-symbolic data in the Atomspace. It may contain any binary object, for example operation (including deep neural networks), collection or value. Grounded value type creators can define custom type, execution and matching logic for the value. There are some grounded atoms in the standard library to deal with numbers or strings, e.g. `(+ 1 2)` is an expression composed of a grounded atom `+`, which refers to an arithmetic operation, and `1` and `2`, which are grounded atoms containing specific values. Adding custom grounded atoms is a standard way for extending MeTTa and its interoperability.

**Symbol**, **Variable**, **Grounded** can be considered as nodes, while **Expression** can be considered as a generalized link. This interpretation of atoms plays an important role in MeTTa applications and Hyperon as a cognitive architecture, but is not essential for understanding MeTTa as a programming language.

MeTTa has optional typing, which is close enough to gradual dependent types, although with some peculiarities. **%Undefined%** is used for untyped expressions, while other types are represented as custom symbols and expressions. **Symbol**, **Variable**, **Grounded**, and **Expression** are metatypes, which can be used to analyze MeTTa programs by themselves. They are subtypes of **Atom**.

## Special symbols

There is a small number of built-in symbols which determine how a MeTTa program will be evaluated:

- Equality symbol `=`  
    defines evaluation rules for expressions and can be read as “can be evaluated as” or “can be reduced to”.
- Colon symbol `:`  
    is used for type declarations.
- Arrow symbol `->`  
    defines type restrictions for evaluable expressions.

These atoms are of `Symbol` metatype, and do not refer to particular binary objects unlike `Grounded` atoms, but they are processed by the interpreter in a special way.