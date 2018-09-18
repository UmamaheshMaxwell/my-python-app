# Please run  python 3.numbers.py in terminal to see the output

"""
There are three numeric types in Python
1. int     - Int, or integer, is a whole number, positive or negative,
             without decimals, of unlimited length
2. float   - Float, or "floating point number" is a number, positive or negative,
             containing one or more decimals
3. complex - Complex numbers have their uses in many applications
             related to mathematics and python provides useful tools
             to handle and manipulate them
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(x)
print(y)
print(z)

# type of the variable
print(type(x))
print(type(y))
print(type(z))

# positive or negative Integer
intValue1 = 1
intValue2 = 2345678987
intValue3 = -45678

print(intValue1, " is of type ", type(intValue1))
print(intValue2, " is of type ", type(intValue2))
print(intValue3, " is of type ", type(intValue3))

# positive or negative float
floatValue1 = 1.154
floatValue2 = 1.0
floatValue3 = -35.59

print(floatValue1, " is of type ", type(floatValue1))
print(floatValue2, " is of type ", type(floatValue2))
print(floatValue3, " is of type ", type(floatValue3))

# Float can also be scientific numbers with an "e" to indicate the power of 10

floatValue4 = 35e3
floatValue5 = 12E4
floatValue6 = -22.4e100

print(floatValue4, " is of type ", type(floatValue4))
print(floatValue5, " is of type ", type(floatValue5))
print(floatValue6, " is of type ", type(floatValue6))

# Complex numbers are written with a "j" as the imaginary part

complexValue1 = 3+5j
complexValue2 = 5j
complexValue3 = -5j

print(complexValue1, " is of type ", type(complexValue1))
print(complexValue2, " is of type ", type(complexValue2))
print(complexValue3, " is of type ", type(complexValue3))
