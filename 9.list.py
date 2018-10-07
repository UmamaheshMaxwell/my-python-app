"""
There are four collection data types in the Python programming language:

List - is a collection which is ordered and changeable. Allows duplicate members.
Tuple - is a collection which is ordered and unchangeable. Allows duplicate members.
Set - is a collection which is unordered and unindexed. No duplicate members.
Dictionary - is a collection which is unordered, changeable and indexed. No duplicate members.

"""

theList = ['apple', 'banana', 'cherry']
print(theList)
print(theList[0])
theList[1] = 'blackcurrant'
print(theList)

# Loop through array of items

for x in theList:
    print(x)

# Check if item exists

if "apple" in theList:
    print('Yes, Apple is in the fruits list')
else:
    print('No item with name Apple')

# Length of array
print(len(theList))

# Add items to the list

theList.append('banana')
print(theList)

# Add item at specified location

theList.insert(3, "orange")
print(theList)

# remove item from list

theList.remove("banana")
print(theList)

# removes the specified index or the last item if index is not specified

theList.pop()
print(theList)

# del keyword removes the specified index

del theList[1]
print(theList)

# del theList  # del keyword can also delete the list completely
# print(theList)  # this will cause an error because "thislist" no longer exists

# clear() method empties the list

theList.clear()
print(theList)

# list() Constructor
# It is also possible to use the list() constructor to make a list.

thisList = list(('Apple', "Banana"))
print(thisList)

# reverse the order of the list
thisList.reverse()
print(thisList)

# sort the order of the list
myNumbers = [6, 7, 5, 1, 4]
print(myNumbers)
myNumbers.sort();
print(myNumbers)