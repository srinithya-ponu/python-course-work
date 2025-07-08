#Defining strings
str1 = "Python"
str2 = "Programming"
print(str1) #Python
print(str2) #Programming

#Operations on strings
str1 = "Python"
str2 = "Programming"
#Concatenation(+)
result = str1 + " " +str2
print(result) #Python Programming
#Repetition(*)
print("Python Programming!  " *2) #Python Programming!  Python Programming!
#Indexing
a = "Python Programming"
print(a[0]) #P
print(a[10]) #g
#Slicing
print(a[0:6]) #python
print(a[:-1]) #Python Programmin
#Membership
print('Python' in a) #True
print('oops' not in a)#True

#Built-in String Functions
a = "Python Programming"
print(len(a)) #18(prints the length of the string)
print(max('APpLe')) #p(highest ASCII value)
print(min('APpLe')) #A(lowest ASCII value)
print(sorted(a)) #[' ', 'P', 'P', 'a', 'g', 'g', 'h','i', 'm', 'm', 'n', 'n', 'o', 'o','r', 'r', 't', 'y']
print(ord('A')) #65(ASCII value of 'A')
print(chr(34)) #"(character for ASCII value 34)

#Case Conversion Methods
a = 'Python'
a.upper() #'PYTHON'(coverts all characters to uppercase)
a.lower() #'python'(coverts all characters to lowercase)
a.capitalize() #'Python'(Capitalizes the first character)
"python programming" . title() #'Python Programming'(Capitalizes the first letter of each word.)
a.swapcase() #'pYTHON'(swaps upper->lower, lower->upper)

#Alignment & Formatting Methods
a = "python"
"python".center(10,"*") #'**python**'(Centers the string within width.)
"py".ljust(5, "-") #'py---'(Left-aligns the string within width.)
"py".rjust(5, "-") #'---py'(Right-aligns the string within width.)

#Search & Find Methods
a= "Python"
a.find("h") #3
a.index("t") #2
a.count("h") #1
a.rfind("h") #3

#String Testing Methods
a= "python"
a.startswith("py") #True
a.endswith("on") #True
a.isalpha() #True
"python99".isalnum() #True
a.islower() #True
"PYTHON".isupper() #True
a.isspace() #False
"Python Program".istitle() #True
"variable1".isidentifier() #True



