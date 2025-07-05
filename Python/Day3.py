# Lists and Tuples

# Lists - A built in data type in Python that allows you to store multiple items in a single variable.
# Lists are mutable, meaning you can change their content without changing their identity.

# Tuples - A built in data type in Python that allows you to store multiple items in a single variable.
# Tuples are immutable, meaning you cannot change their content once they are created.

marks = [90, 80, 70, 60, 50]
print("Marks list : ", marks)
print(type(marks))  # type is used to find the type of the variable.
marks[0] = 95
print(marks[0:3])

# List methods

marks.append(100)  # Adds an item to the end of the list.
marks.insert(2, 75)  # Inserts an item at a given position.
marks.remove(60)  # Removes the first item with the specified value.
marks.pop(1) # Removes the item at the given position in the list, or removes the last item if no index is specified.
marks.sort() # Sorts the list in ascending order.
marks.sort(reverse=True) # Sorts the list in descending order.
marks.reverse() # Reverses the order of the list.


# Tuples
marks_tuple = (90, 80, 70, 60, 50)
print("Marks tuple : ", marks_tuple)
print(type(marks_tuple))  # type is used to find the type of the variable.

# Tuple methods
marks_tuple.index(80)  # Returns the index of the first item with the specified value.
marks_tuple.count(60)  # Returns the number of times a specified value occurs in a tuple.
