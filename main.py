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
class MyError(Exception):
    pass

raise MyError()