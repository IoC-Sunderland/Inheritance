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


# Composition
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def calculate_annual_salary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        # Create an instance of the Salary class
        # to enable Composition
        self.salary_object = Salary(pay, bonus)
    
    def annual_salary(self):
        return self.salary_object.calculate_annual_salary()

e = Employee('Average Joe', 32, 25000, 2500)
print(e.annual_salary())
