# Dictionary and Set 

# Dictionary - A collection of key-value pairs. They are unordered, changeable, and indexed. Keys must be unique and immutable.

# Set - An unordered collection of unique elements. They are mutable and do not allow duplicate values.

# Dictionary Example

my_dict = {
    "name" : "Shlok srivastava",
    "age" : 20,
    "is_student" : True,
    "courses" : ["Python", "Java", "C++", "JavaScript"],
    "address" : {
        "state" : "Bihar",
        "city" : "Patna"
    }
}

print(my_dict)
print('-----------------------')
print(type(my_dict))
print('-----------------------')

for i in my_dict:
    print(i, ":", my_dict[i])

print('-----------------------')

# Dictionary Methods
print(my_dict.keys())
print('-----------------------')
print(list(my_dict.values()))
print('-----------------------')
print(my_dict.items()) # Returns a view object that displays a list of a dictionary's key-value tuple pairs.
print('-----------------------')
print(my_dict.get("name")) # Returns the value of the specified key
print('-----------------------')

hobby = {
    "hobby": "Coding",
}
print(my_dict.update(hobby)) # Adds a new key-value pair to the dictionary
print(my_dict)
print('-----------------------')

# Set Example

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
null_set = set()  # Creating an empty set
print(my_set)
print(type(my_set))

# Set Methods
print('-----------------------')
print(my_set.add(11))  # Adds an element to the set
print(my_set.remove(5)) # Removes an element from the set
print(my_set.pop())  # Removes and returns an arbitrary element from the set
print(my_set.clear())  # Removes all elements from the set
print(my_set)

my = {1, 2, 3, 4, 5}
your = {4, 5, 6, 7, 8}
# Set Operations
print('-----------------------')
print(my.union(your))  # Returns a set that contains all elements from both sets
print(my.intersection(your))  # Returns a set that contains elements common to both sets