# Type casting in python is done using constructor functions

"""
int()  -  constructs an integer number from an integer literal,
          a float literal (by rounding down to the previous whole number), or
          a string literal (providing the string represents a whole number).

float() - constructs a float number from an integer literal,
          a float literal or a string literal (providing the
          string represents a float or an integer).

str()   - constructs a string from a wide variety of data types,
          including strings, integer literals and float literals.
"""

# Integers
intValue1 = int(1)    # x will be 1
intValue2 = int(2.8)  # y will be 2
intValue3 = int("3")  # z will be 3

print(intValue1)
print(intValue2)
print(intValue3)

# Floats

floatValue1 = float(1)      # x will be 1.0
floatValue2 = float(2.8)    # y will be 2.8
floatValue3 = float("3")    # z will be 3.0
floatValue4 = float("4.2")  # w will be 4.2


print(floatValue1)
print(floatValue2)
print(floatValue3)
print(floatValue4)

# Strings

stringValue1 = str("s1")  # x will be 's1'
stringValue2 = str(2)     # y will be '2'
stringValue3 = str(3.0)   # z will be '3.0'

print(stringValue1)
print(stringValue2)
print(stringValue3)