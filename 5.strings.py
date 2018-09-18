"""
 String literals in python are surrounded by either
 single quotation marks, or double quotation marks

 **************************************************

 Like many other popular programming languages, strings
 in Python are arrays of bytes representing unicode characters.
 However, Python does not have a character data type,
 a single character is simply a string with a length of 1.
 Square brackets can be used to access elements of the string.

"""

# Get the character at position 1

message1 = "Hello World"
print(message1[1])  # (remember that the first character has the position 0)

# Substring. Get the characters from position 2 to position 5 (not included)

message2 = "Hello World"
print(message2[2:5])

# The strip() method removes any whitespace from the beginning or the end

message3 = " Hello, World! "
print(message3.strip())

# The len() method returns the length of a string

message4 = "Hello World"
print(len(message4))

# The lower() method returns the string in lower case

message5 = "Hello World"
print(message5.lower())

# The upper() method returns the string in upper case

message6 = "Hello World"
print(message6.upper())

# The replace() method replaces a string with another string

message7 = "Hello World"
print(message7.replace('H', 'C'))

# The split() method splits the string into substrings if it finds instances of the separator

message8 = 'Hello, World'
print(message8.split(','))  # returns ['Hello', ' World!']
