"""
Classes and Objects

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
"""

# Create a Class
# To create a class, use the keyword class


class Sample:
    x = 5


print(Sample)

# Create Object
# Now we can use the class named myClass to create objects

obj = Sample()
print(obj.x)

# The __init__() Function
# The examples above are classes and objects in their simplest form,
# and are not really useful in real life applications.
#
# To understand the meaning of classes we have to understand the built-in __init__() function.
#
# All classes have a function called __init__(), which is always
# executed when the class is being initiated.
#
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Uma", 36)

print(person1.name)
print(person1.age)

# Note: The __init__() function is called automatically every time
#       the class is being used to create a new object.

# Note: The self parameter is a reference to the class instance itself,
# and is used to access variables that belongs to the class.

# Object Methods
# Objects can also contain methods. Methods in objects are functions
# that belongs to the object.


class Student:
    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    def getfullname(self):
        return self.firstName + " " + self.lastName


student1 = Student("Umamaheswararao", "Meka")
print(student1.getfullname())


class Vehicle:
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def getvehicle(anything):
        return anything.type + " " + anything.color


vehical = Vehicle('Brezza', 'red')
print(vehical.getvehicle())

# Modify Object Properties
# You can modify properties on objects like this:

vehical.type = "Vitara Brezza"
print(vehical.getvehicle())

# Delete Object Properties
# You can delete properties on objects by using the del keyword:

# del vehical.color
# print(vehical.getvehicle())

# Delete Objects
# You can delete objects by using the del keyword:

# del vehical
# print(vehical)



















