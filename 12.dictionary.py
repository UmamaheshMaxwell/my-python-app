"""
Dictionary
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have
keys and values.

"""

theDict = {
    "brand": "Maruthi",
    "model": "Brezza",
    "year": 2018
}
print(theDict)

# Accessing Items
# You can access the items of a dictionary by referring to its key name

model = theDict["model"]
print(model)

# There is also a method called get() that will give you the same result:
model = theDict.get('model')
print(model)

# Change Values
# You can change the value of a specific item by referring to its key name:
theDict["brand"] = "Maruth Suzuki"
print(theDict)

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are
# the keys of the dictionary, but there are methods to
# return the values as well.

# Just Keys
for item in theDict:
    print(item)

# Values
for key in theDict:
    print(theDict[key])

# You can also use the values() function to return values of a dictionary:
for value in theDict.values():
    print(value)

# Loop through both keys and values, by using the items() function:
for x, y in theDict.items():
    print(x, y)

# To determine if a specified key is present in a dictionary use the in keyword:

if "model" in theDict:
    print('yes, the model is present')

# To determine how many items (key-value pairs) a dictionary have,
# use the len() method.
print(len(theDict))

# Adding Items
# Adding an item to the dictionary is done by using a new index
# key and assigning a value to it:

theDict["color"] = "Red"
theDict["city"] = "Hyderabad"
theDict["state"] = "Telangana"
theDict["country"] = "India"
print(theDict)

# Removing Items
# There are several methods to remove items from a dictionary:

# The del keyword removes the item with the specified key name:
del theDict["city"]
print(theDict)

# The pop() method removes the item with the specified key name:
theDict.pop('state')
print(theDict)

# The popitem() method removes the last inserted item
# (in versions before 3.7, a random item is removed instead):
theDict.popitem()
print(theDict)

# The del keyword can also delete the dictionary completely:
# del theDict
# print(theDict)

# The clear() keyword empties the dictionary:
theDict.clear()
print(theDict)


# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary:

thisdict = dict(brand="Maruthi", model="Brezza", year=2018)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
