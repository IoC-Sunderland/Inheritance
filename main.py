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
    # Overrid the print_mew method
    def print_me(self):
        return f"ID: {self.id}\nName: {self.name}"

a = New(123, 'Gav')

print(a.print_me())

# Multiple Inheritance
