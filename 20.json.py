"""
JSON

JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

"""

# Python has a built-in package called json, which can be use to work with JSON data.

import json

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York" }'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using
# the json.dumps() method.

# a Python object (dict):
x = {
  "name": "Uma",
  "age": 36,
  "city": "Bangalore"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# You can convert Python objects of the following types, into JSON strings:
#
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


