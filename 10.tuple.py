"""
Tuple
A tuple is a collection which is ordered and unchangeable.
In Python tuples are written with round brackets.
"""

thisTuple = ('apple', 'banana', 'cherry')
print(thisTuple)

# Access tuple items
print(thisTuple[1])

# Change tuple values
# thisTuple[1] = "blackcurrant"
# print(thisTuple)

# Loop through a tuple
for x in thisTuple:
    print(x)

# Check if item exits

if "apple" in thisTuple:
    print('Yes, Apple is present in this list')
else:
    print('There is no item with this list')

# Get Tuple length

print(len(thisTuple))

# Add Items
# Once a tuple is created, you cannot add items to it.
# Tuples are unchangeable.

# thisTuple[3] = "orange"
# print(thisTuple)

# Remove Items
# Tuples are unchangeable, so you cannot remove items from it,
# but you can delete the tuple completely

#  del keyword can delete the tuple completely
# del thisTuple
# print(thisTuple)

# tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
newTuple = tuple(('apple', 'banana'))
print(newTuple)

