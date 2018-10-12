"""
Functions
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

"""

# Creating a Function
# In Python a function is defined using the def keyword:

def callMe():
    print('Hey Did you call me ?')

# Calling a Function
# To call a function, use the function name followed by parenthesis:
callMe()

# Parameters
# Information can be passed to functions as parameter.
#
# Parameters are specified after the function name, inside the parentheses.
# You can add as many parameters as you want, just separate them with a comma.
#
# The following example has a function with one parameter (firstName).
# When the function is called, we pass along a first name,
# which is used inside the function to print the full name:

def wishHello(firstName):
    print('Hello ' + firstName)

wishHello('Umamaheswararao Meka')
wishHello("uma@uma.com")

# Default Parameter Value
# The following example shows how to use a default parameter value.
#
# If we call the function without parameter, it uses the default value:

def displayCountry(country ="Norway"):
    print("I am from " + country)

displayCountry('India')
displayCountry('Australia')
displayCountry('Canada')
displayCountry()
displayCountry('United States')

# Return Values
# To let a function return a value, use the return statement:

def multiply(x):
    return 2 * x

total1 = multiply(5)
print(total1)

total2 = multiply(4)
print(total2)

