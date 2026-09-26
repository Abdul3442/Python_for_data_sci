## In this chapter we will discuss the conditional logics with easy examples. Lets discuss it from beginning.
# What is conditional logics?
# Conditional logics are used to make decisions in a program based on certain conditions. In Python, you can use the if statement to execute a block of code if a certain condition is true. You can also use the else statement to execute a block of code if the condition is false. Additionally, you can use the elif statement to check multiple conditions in a single if-else block.
# Here is an example of how to use conditional logics in Python:
print (4==4) # This line of code will print the result of the comparison operation (4 == 4) to the console, which is True.
print (4!=4) # This line of code will print the result of the comparison operation (4 != 4) to the console, which is False.
print (4<5) # This line of code will print the result of the comparison operation (4 < 5) to the console, which is True.
print (4>5) # This line of code will print the result of the comparison operation (4 > 5) to the console, which is False.
print (4<=5) # This line of code will print the result of the comparison operation (4 <= 5) to the console, which is True.
print (4>=5) # This line of code will print the result of the comparison operation (4 >= 5) to the console, which is False.
#Remember above codes are used only example purpose and to understand the conditional logics. In real world we use it in different ways. Lets discuss the some advance examples now:    

if 4==4:
    print ("This is true") # This line of code will print the message "This is true" to the console if the condition (4 == 4) is true)
if 3>6:
    print ("This is true") # This line of code will not be executed because the condition (3 > 6) is false.
if 4>=7:
    print ("This is true") # This line of code will not be executed because the condition (4 >= 7) is false.
if 4!=4:
    print ("This is true") # This line of code will not be executed because the condition (4 != 4) is false.

# These are the some intermediate examples of logical operators.

# Now we will learn more applications of logicals operators:
# Example 01
abdul_age=20
if abdul_age>=18:
    print ("Abdul is eligible to vote") # This line of code will print the message "Abdul is eligible to vote" to the console if the condition (abdul_age >= 18) is true.
# Example 2
atiq_age=5 
age_at_school=4
if atiq_age>=age_at_school:
    print ("Atiq is eligible to go to school") # This line of code will print the message "Atiq is eligible to go to school" to the console if the condition (atiq_age >= age_at_school) is true.   

# Now we use Input operators and logics both:
#Example 1
abdul_age=int(input("Enter Abdul's age: "))
if abdul_age>=18:
    print ("Abdul is eligible to vote")
    
# Example 2
atiq_age=int(input("Enter Atiq's age: "))
age_at_school=int(input("Enter the age at which a child can go to school: "))
if atiq_age>=age_at_school:
    print ("Atiq is eligible to go to school")

# Hope you learn alot from this chapter. If you have any questions or feedback, please feel free to reach out to me. I would love to hear from you. Happy coding!
# Follow me on Linkedin: www.linkedin.com/in/abdulrehman2002