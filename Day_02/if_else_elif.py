# if, else and elif are comes under the category of conditional logics. In this chapter we will discuss these in detail. Lets start:

# The if statement is used to test a specific condition. If the condition is true, then the block of code inside the if statement will be executed. If the condition is false, the block of code will be skipped.

# Let's see an example of if statement:
x = 10
if x > 5:
    print("x is greater than 5") 

# In the above example, the condition x > 5 is true, so the block of code inside the if statement will be executed and "x is greater than 5" will be printed.

# Example of if statement with false condition:
y = 3
if y > 5:
    print("y is greater than 5")

# In the above example, the condition y > 5 is false, so the block of code inside the if statement will be skipped and nothing will be printed. 

# Example of if statement with else:
z = 2
if z > 5:
    print("z is greater than 5")
else:
    print("z is not greater than 5")

# In the above example, the condition z > 5 is false, so the block of code inside the else statement will be executed and "z is not greater than 5" will be printed.

# Example of if statement with elif:
a = 7
if a > 10:
    print("a is greater than 10")
elif a > 5:
    print("a is greater than 5 but less than or equal to 10")
else:
    print("a is not greater than 5")
# In the above example, the condition a > 10 is false, so the block of code inside the elif statement will be executed and "a is greater than 5 but less than or equal to 10" will be printed.

# Lets understand with more advance example:
# Example of if statement with multiple elif:
b = 15
if b > 20:
    print("b is greater than 20")
elif b > 10:
    print("b is greater than 10 but less than or equal to 20")
else:
    print("b is not greater than 10")

# Another example of if statement: 
req_age_at_school=10 
atiq_age=6
if atiq_age>=req_age_at_school:
    print("Atiqa can go to school") 
    
elif atiq_age<req_age_at_school:
    print("Atiqa cannot go to school")
    
else:
    print("Atiqa cannot go to school")
    
# In the above example, the condition atiq_age >= req_age_at_school is false, so the block of code inside the elif statement will be executed and "Atiqa cannot go to school" will be printed.  
# However, the else statement will never be executed because the elif condition is already true.
# This is how if, else and elif statements work in Python. You can use them to control the flow of your program based on different conditions.

# Here is a summary of the if, else and elif statements:
# - if statement: used to test a specific condition. If the condition is true, the block of code inside the if statement will be executed. If the condition is false, the block of code will be skipped.
# - else statement: used to execute a block of code if the condition in the if statement is false. It is optional and can be used after an if statement.
# - elif statement: used to test multiple conditions. It is optional and can be used after an if statement. If the condition in the if statement is false, the elif statement will be tested. If the condition in the elif statement is true, the block of code inside the elif statement will be executed. If the condition in the elif statement is false, the block of code inside the else statement will be executed.

# Here is a simple flowchart to understand the if, else and elif statements:

# Hope this helps you to understand the if, else and elif statements in Python. You can use them to control the flow of your program based on different conditions. 

# I hope you enjoyed this chapter. In the next chapter, we will discuss functions in Python. Stay tuned!
# Thank you for reading this chapter. If you have any questions or feedback, please feel free to reach out to me. I would love to hear from you! Happy coding!

# Follow me on linkedin: www.linkedin.com/in/abdulrehman2002