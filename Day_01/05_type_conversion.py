# Type Conversion in Python
# Type conversion is the process of converting a value from one data type to another. In Python, you can use built-in functions to convert between different data types. The most commonly used type conversion functions are int(), float(), str(), and bool(). Here is an example of how to use these functions:
# Convert a string to an integer
x = int("10")
print(x) # Output: 10
# Convert a string to a float
y = float("3.14")
print(y) # Output: 3.14 

# Lets discuss some more examples in detail:
x="10"
print (type(x)) # This line of code will print the data type of the variable x

y=15
print (type(y))

a=str(3)
print (type(a))

# Lets discuss the type of conversion: 
# Implicit and Explicit conversion

# Implicit type conversion: 

# Implicit type conversion, also known as type coercion, is the automatic conversion of one data type to another by the Python interpreter. This occurs when you perform operations on different data types, and Python automatically converts one of the operands to a compatible data type. For example:
x = 5 # integer
y = 3.14 # float
z = x + y # The integer x is implicitly converted to a float, and then added to y
print(z) # Output: 8.14
print(type(z)) # Output: <class 'float'>

#  Lets discuss one more example of implicit type conversion:
x = 10 # integer
y = 2.5 # float
z = x + y # The integer x is implicitly converted to a float, and then added to y
print(z) # Output: 12.5
print(type(z)) # Output: <class 'float'>

# Explicit type conversion:
# Explicit type conversion, also known as type casting, is the manual conversion of one data type to another using built-in functions. This allows you to control the data types of your variables and ensure that they are compatible for operations. For example:
x = 5 # integer
y = 3.14 # float
z = int(y) # The float y is explicitly converted to an integer using the int() function
print(z) # Output: 3

# Lets discuss one more example of explicit type conversion:
x = "10" # string
y = int(x) # The string x is explicitly converted to an integer using the int() function
print(y) # Output: 10
print(type(y)) # Output: <class 'int'>

# Hope you are enjoying learning python for data science. If you have any questions or feedback, please feel free to reach out to me. I would love to hear from you. Happy coding!  
# Follow me on Linkedin: www.linkedin.com/in/abdulrehman2002