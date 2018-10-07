"""
Set
A set is a collection which is unordered and unindexed.
In Python sets are written with curly brackets.
"""

thisSet = {'apple', 'banana', 'cherry'}
print(thisSet)

# Access Items

for x in thisSet:
    print(x)

# Check if "item" is present in the set

print("banana" in thisSet)

if "banana" in thisSet:
    print('Yes')

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.

# Add Items
# To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.

thisSet.add('orange')
print(thisSet)

thisSet.update(['mango', 'grapes'])
print(thisSet)

# Get the Length of a Set
# To determine how many items a set have, use the len() method

print(len(thisSet))

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# Note: If the item to remove does not exist, remove() will raise an error.

thisSet.remove('banana')
print(thisSet)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

thisSet.discard('cherry')
print(thisSet)


thisSet.discard('cherry1')
print(thisSet)


# You can also use the pop(), method to remove an item,
# but this method will remove the last item. Remember
# that sets are unordered, so you will not know what item that gets removed.

# The return value of the pop() method is the removed item.
item = thisSet.pop()
print(item)
print(thisSet)

# The clear() method empties the set
# thisSet.clear()
# print(thisSet)

# The del keyword will delete the set completely
# del thisSet
# print(thisSet)

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)