# Inheritance

We implement inheritance by creating a sub class that inherit attributes and methods from a base class.

This models an <strong> is a </strong> relationship.

E.g. a car <strong> is a </strong> vehicle.

<img src="img/Inheritance.png" width="200" height ="300">

# Composition
We implement composition by combining objects of other types.

Classes that contain objects of other classes are composites.

Classes that are used to create more complex types are referred to as components.

This models a <strong> has a </strong> relationship.

E.g. a car <strong> has a </strong> engine.

<img src="img/Composition.png" width="200" height ="300">

# Abstract Base Classes
Classes that exist to be inherited, but you do not instantiate them.

# super()
There are two typical use cases for super. In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of super in other programming languages.

The second use case is to support cooperative multiple inheritance in a dynamic execution environment(doc.python.org).

# Multiple Inheritance
Python supports multiple inheritance (inheriting from more than one class)

Few languages enable you to inherit from more than one class, instead they implement multiple interfaces.
