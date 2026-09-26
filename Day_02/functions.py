# In this chapter we will discuss about functions in python. 
# Functions are a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# print() is a built-in function in Python. It is used to print the specified message to the screen, or other standard output device.
print("Hello, World!")

# defining a function
def greet(name):
    print("Hello, " + name + "!")

# calling a function
greet("Abdul")
greet("Atiq")
greet("Ayesha")

# In the above example, we defined a function called greet() that takes one parameter called name. When we call the function greet() and pass a name as an argument, it prints a greeting message to the screen.

# You can also return a value from a function using the return statement. Here is an example:
def add(a, b):
    return a + b

# calling the function and storing the returned value
result = add(5, 3)
print(result)  # Output: 8 

# In the above example, we defined a function called add() that takes two parameters a and b. When we call the function add() and pass two numbers as arguments, it returns the sum of those numbers. We store the returned value in a variable called result and print it to the screen.

# function with conditional statements
def check_age(age):
    if age >= 18:
        return "You are eligible to vote."
    elif age < 18 and age >= 0:
        return "You are not eligible to vote."
    else:
        return "Invalid age."

# def function of future age
def future_age(current_age, years):
    if current_age < 0 or years < 0:
        return "Invalid age or years."
    else:
        return current_age + years
    
# In the above example, we defined a function called check_age() that takes one parameter called age. It uses if, elif, and else statements to check the age and return an appropriate message. We also defined a function called future_age() that takes two parameters current_age and years. It checks if the current_age or years is negative and returns an appropriate message. Otherwise, it returns the future age by adding current_age and years. 

# In the next chapter, we will discuss about loops in Python. Stay tuned!
# Thank you for reading this chapter. I hope you enjoyed it and learned something new about functions in Python. Happy codding!
# Follow me on linkedin: www.linkedin.com/in/abdulrehman2002
                     