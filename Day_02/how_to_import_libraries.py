# In this chapter we will discuss how to import libraries in Python. \

# Libraries are a collection of pre-written code that can be used to perform specific tasks. 
# Python has a large number of built-in libraries that can be imported and used in your code.

# There are two ways to import libraries in Python:
# 1. Import the entire library
# 2. Import specific functions or classes from a library

# Let's discuss both ways of importing libraries in Python.

# 1. Import the entire library:
# To import the entire library, you can use the import statement followed by the name of the library.
# For example, to import the math library, you can use the following code:
import math
print(math.pi)

# In the above example, we imported the entire math library and used the pi constant from the math library to print the value of pi.

#  Lets discuss some more examples.
# Example of importing the entire random library:
import random
print(random.randint(1, 10))

# In the above example, we imported the entire random library and used the randint() function from the random library to generate a random integer between 1 and 10.

# 2. Import specific functions or classes from a library:
# To import specific functions or classes from a library, you can use the from keyword followed by the name of the library and the import statement followed by the name of the function or class you want to import.
# For example, to import the sqrt() function from the math library, you can use the following code:
from math import sqrt
print(sqrt(25))
# In the above example, we imported the sqrt() function from the math library and used it to calculate the square root of 25.

# Example of importing specific functions from the random library:
from random import randint, choice
print(randint(1, 10))
print(choice(["apple", "banana", "cherry"]))
# In the above example, we imported the randint() and choice() functions from the random library and used them to generate a random integer between 1 and 10 and to select a random item from a list of fruits.

# Thank you for reading this chapter. I hope you enjoyed it and learned something new about importing libraries in Python. Happy coding!
# Follow me on linkedin: www.linkedin.com/in/abdulrehman2002
