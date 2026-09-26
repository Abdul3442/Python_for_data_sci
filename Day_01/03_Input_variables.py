# What is input variables?
# Input variables are used to take input from the user during the execution of a program. In Python, you can use the built-in input() function to get input from the user. The input() function reads a line of text entered by the user and returns it as a string. You can also specify a prompt message to display to the user before they enter their input.
# Here is an example of how to use the input() function in Python:
name = input("Please enter your name: ")
print("Hello, " + name + "!") # In this example, the input() function prompts the user to enter their name. The user's input is then stored in the variable name, and a greeting message is printed to the console using the value of the name variable.
# + shows the concatenation of strings in python. It is used to combine two or more strings into a single string. In the example above, the + operator is used to concatenate the greeting message "Hello, " with the value of the name variable and the exclamation mark "!" to create a complete greeting message.

# There are 2 types of input variables in python:
# simple input variable and 2nd stage input variable. 
# Simple input variable is used to take input from the user and store it in a variable. The input() function returns the user's input as a string, so if you want to store the input as a different data type (e.g., integer or float), you need to convert it using the appropriate type conversion function (e.g., int() or float()).
# Here is an example of how to use the input() function to take input from the user and store it in a variable:
age = input("Please enter your age: ")
age = int(age) # Convert the input to an integer
print("You are " + str(age) + " years old.")

# 3rd stage input function is used to take input from the user and store it in a variable. The input() function returns the user's input as a string, so if you want to store the input as a different data type (e.g., integer or float), you need to convert it using the appropriate type conversion function (e.g., int() or float()).
# Here is an example of how to use the input() function to take input from the user and store it in a variable:
height = input("Please enter your height in meters: ")
height = float(height) # Convert the input to a float
print("Your height is " + str(height) + " meters.")

# How to find the class? Use the built-in type() function to find the class of a variable in python. The type() function takes a variable as an argument and returns its data type. Here is an example:
age = 25
print(type(age)) # Output: <class 'int'>

# Hope you are enjoying learning python for data science. If you have any questions or feedback, please feel free to reach out to me. I would love to hear from you. Happy coding!  
# Follow me on Linkedin: www.linkedin.com/in/abdulrehman2002