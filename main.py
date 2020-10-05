# All Python classes inherit from object implicitly.

# Note: In Python 2 we need to explicitly inherit from object - see below:

class MyClass(object):
    pass

c = MyClass()

# All members inherited from object
print(dir(c))

# Except
class MyError():
    pass

# Will produce TypeError not custom error
# raise MyError()

# Needs to inherit from Exception
# class MyError(Exception):
#   pass

# raise MyError()

# Abstract Class Example
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    # Abstract method must be overridden by sub class
    @abstractmethod
    def print_me(self):
        pass

# Below will throw error
# a = MyAbstractClass()

# Create New class and inherit from Abstract Base Class
class New(MyAbstractClass):
    # Override the print_mew method
    def print_me(self):
        return f"ID: {self.id}\nName: {self.name}"

a = New(123, 'Gav')

print(a.print_me())

# super()
class Base():
    def __init__(self, name):
        print('Base __init__ called...', name)


class Base_Two():
    def __init__(self, name):
        print('Base_Two __init__ called...', name)


# Multiple Inheritance
class Child(Base, Base_Two):
    def __init__(self):
        print('Child __init__ called...')
        super().__init__('Child')

print('>>> super() example:\n')
a = Child()

# MRO - Method Resolution Order
from pprint import pprint
pprint(Child.__mro__)
