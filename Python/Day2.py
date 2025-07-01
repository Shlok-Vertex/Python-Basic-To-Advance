# Strings statement.

str1 = "This is a string"
str2 = 'This is also a string'
str3 = """This is a string that spans multiple lines"""

# escape sequence characters - \n, \t, \\, \'

name1 = "Shlok"
name2 = "Srivastava"
print("Hello!... " + name1 + " " + name2)  # Concatenation of strings
print(len(name1),len(name2))  # Length of the string

# Slicing of strings
print(name1[0:3])  # Slicing from index 0 to 2. It not include last index.
print(name2[0:5])  # Slicing from index 0 to 4. 
print(name1[0:])  # Slicing from index 0 to end.
print(name2[:5])  # Slicing from start to index 4.


# String methods
name1.capitalize()  # Capitalizes the first letter of the string
name2.upper()  # Converts the string to uppercase
name1.lower()  # Converts the string to lowercase
name2.title()  # Converts the first letter of each word to uppercase
print(name1.replace("S", "A"))  # Replaces the first occurrence of 'S' with 'A'
name2.find("S")  # Finds the first occurrence of 'S' in the string
name1.count("S")  # Counts the number of occurrences of 'S' in the string
print(name2.split("a"))  # Splits the string into a list of strings using 'a' as the delimiter
name1.strip()  # Removes leading and trailing whitespace from the string

# Conditional statements.

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# nesting of conditional statements.

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
    if age >= 30:
        print("You are in your thirties or older.")
else:
    print("You are a senior citizen.")
    if age >= 80:
        print("You are in your eighties or older.")

