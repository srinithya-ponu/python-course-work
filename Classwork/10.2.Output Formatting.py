#Output Formatting

#The print() function in python output text, numbers, or any other data type to console.
#Basic Syntax : print(object, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

#Basic examples of print()
#a)Printing Text
print("Hello World!") #Hello World!
#b)Printing multiple items
name = "Abhishek"
age = 26
print("Name:", name, "Age:", age)   #Name: Abhishek Age: 26
#c)Using sep to change the Seperator
print("16", "07", "2025", sep="-")   #16-07-2025
#d)Using end to control Line Endings
print("Hello,", end=" ")
print("World!")   #Hello, World!

#Printing special Characters
#a)New Line(\n):
print("hi \nbye")    #hi 
                     #bye

#b)Tab(\t)
print("course:\tDS")  #course:	DS

#Output Formatting

#1. Using Commas (Simple Print Method)
#This is the most basic way to print multiple items. When you separate items with commas in the print() function, Python adds a space between them automatically.
name = "Jashwanth"
age = 23
city = "USA"
print("Name:", name, "Age:", age, "City:", city)    #Name: Jashwanth Age: 23 City: USA
                                                                     
#2. Using Modulo Operator (% Formatting)
#This is an older method, similar to C-style formatting. You use % followed by format specifiers like %s (string), %d (integer), %f (float), etc.
name = "Shobith"
age = 18
city = "Telangana"
marks = 98.9
print(f"name: %s | age: %d  | city:%s | marks: %.2f" % (name,age,city,marks))            #name: Shobith | age: 18  | city:Telangana | marks: 98.90  

#3.Using f-strings (Formatted String Literals) 
#This is the most modern and recommended method. Add an f before the string and use curly braces {} to insert variables directly.
name = "Jaideep"
age = 14
city = "Karnataka"
marks = 99.9
print(f"Name: {name} | age: {age} | city: {city} | marks: {marks}")              #Name: Jaideep | age: 14 | city: Karnataka | marks: 99.9

#4. Using str.format() Method
#This method works in both Python 2 and 3. You use {} as placeholders and call .format() with the variables you want to insert.
Name = "Haripreeth"
Age = 11
City = "andhrapradesh"
Marks = 98.9
print("Name: {} | Age: {} |City: {} | Marks: {:.1f}".format(Name, Age,City,Marks))                 #Name: Haripreeth | Age: 11 |City: andhrapradesh | Marks: 98.9
