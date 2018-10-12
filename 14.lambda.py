"""
Lambda
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

"""

# A lambda function that adds 10 to the number passed
# in as an argument, and print the result:
add = lambda a: a + 10
print(add(5))

# Lambda functions can take any number of arguments:
# A lambda function that multiplies argument a with
# argument b and print the result:
multiply = lambda a, b: a * b
print(multiply(5, 6))

# A lambda function that sums argument a, b, and c
# and print the result:
addition = lambda a, b, c: a + b + c
print(addition(5, 6, 2))


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as
# an anonymous function inside another function.

# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:

def calculateValue(x):
    return lambda a: a + x

getTotal = calculateValue(10)
print(getTotal(5))

# create a function definition to make a function that always
# doubles the number you send in

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
