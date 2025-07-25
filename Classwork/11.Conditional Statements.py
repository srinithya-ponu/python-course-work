#Conditional Statements
#Conditional statements allow a program to execute certain pieces of code based on whether a specific condition is True or False. They help in decision-making processes within the code.

#In Python, the main types of conditional statements are:
#1. if Statement
#2. if-else Statement
#3. if-elif-else Statement
#4. Nested Conditional Statements

#1. if Statement:

#The if statement is the most basic conditional statement. It checks if a condition is True. If it is, the block of code under the if statement is executed. If the condition is False, the code is skipped.
#Syntax:
   #if condition:
      # Code to execute if the condition is True

#Example1:(Check if a number is positive)
a=100
if a>0:
    print("a is positive")     #a is positive

#Example2:(Check if today is a weekend)
day = "Sunday"

if day == "Sunday":
    print("It's a holiday!")   #It's a holiday!


#2. if-else Statement:

#The if-else statement adds an alternative path. If the if condition is True, the first block runs. If it is False, the else block runs.
#Syntax:
    #if condition:
       # Code to execute if the condition is True
    #else:
       # Code to execute if the condition is False


#Example 1:(Even or Odd Number)
num = 19

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")         #Odd number


#Example 2:(Check if a word is long)
word = "elephant"

if len(word) > 5:
    print("It's a long word")
else:
    print("It's a short word")   #It's a long word


#3. if-elif-else Statement
#When you have multiple conditions to check, the if-elif-else structure is used.
# The program checks conditions one by one.
# As soon as a condition evaluates to True, the corresponding code block runs, and the remaining conditions are skipped.
# The else block is optional and only runs if none of the previous conditions are met.

#Syntax
    #if condition1:
       # Code if condition1 is True
    #elif condition2:
       # Code if condition2 is True
    #elif condition3:
       # Code if condition3 is True
    #else:
       # Code if none of the conditions are True

#Example1:( Check Time of Day)
hour = 14

if hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
else:
    print("Good evening")       #Good afternoon

#Example2:(Grading System)
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")          #Grade: B

    
#4. Nested Conditional Statements
#Nested conditional statements are when an if statement is placed inside another if or else block. This structure is useful when you need to check a condition only if another condition is already met.

#Syntax:
    #if condition1:
       # Code if condition1 is True
       #if condition2:
          # Code if both condition1 and condition2 are True
       #else:
          # Code if condition1 is True but condition2 is False

    #else:
       # Code if condition1 is False

#Example1:(Check Login Credentials)
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Username not found")     #Login successful

#Example2:(Weather Clothing Suggestion)
is_raining = True
temperature = 15

if is_raining:
    print("Take an umbrella")
    if temperature < 20:
        print("Wear a jacket")
else:
    print("No rain today")         #Take an umbrella  #Wear a jacket

    



