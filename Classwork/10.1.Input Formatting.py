#Input Formatting
#Python's input() function is used to take input from the user during program execution. By default, it returns a string. We often convert the input into int, float, list, tuple, set, or dict as needed.

#1. String Input
student = input("Enter your name: ")
print(student)                               #Enter your name: string input.  Output=string input

#2. Integer Input= Use case: Age, quantity, mobile number, number of items in cart.
items = int(input("Enter the number of items: "))                #Enter the number of items: 23
print(items)                                                     #23

#3. Float Input= Use case: Price, temperature, discount, rating.
price = float(input("Enter the product price: "))               #Enter the prodect price: 96.2
print(price)                                                    # 96.2

#4. Input as List (Space-separated)=Use case: List of names, marks, or product IDs.
courses = input("Enter courses name(space_separated): ").split()          #Enter courses name(space_separated):  python ds
print(courses)                                                            #['python', 'ds']

#5.Input as List (Comma-separated)=Use case: Tags, emails, product categories.
courses = input("Enter courses name(comma_separated): ").split(',')          #Enter courses name(comma_separated): java,embedded,banking
print(courses)                                                               #['vlsi', 'embedded', 'banking']

#6. List of Integers=Use case: Marks, product prices, IDs.
numbers = list(map(int, input("Enter numbers: ").split()))                   #Enter numbers: 1 2 3 4 5 6
print(numbers)                                                               #[1, 2, 3, 4, 5, 6]

#7. List of Floats=Use case: Sensor readings, weights, product prices.
prices = list(map(float, input("Enter prices: ").split()))                  #Enter prices: 6.8 64.4 19.6 75.1
print(prices)                                                               #[6.8, 64.4, 19.6, 75.1]

#8. Tuple Input=Use case: Coordinates, dimensions (length, width, height).
dimensions = tuple(map(int, input("enter length, width, height: ").split()))     #Enter length, width, height: 99 48 34
print(dimensions)                                                                #(99, 48, 34)

#9.Set Input=Use case: Selected image IDs where duplicates must be removed (e.g., in a photo-sharing app).
selected_ids = set(map(int, input("Enter selected image IDS:").split()))           #Enter selected image IDS:309 429 205 206 157
print(selected_ids)                                                               #{205, 206, 429, 309, 157}

#10. Dictionary Input using eval()=Use case: When entering structured data like configuration settings or user profiles.
profile = eval(input("Enter user profile as a dictionary: "))                      #Enter user profile as a dictionary: {'name': 'Abhishek', 'age': 21,' course': 'datascience'}
print(profile)                                                                     #{'name': 'Abhishek', 'age': 21, ' course': 'datascience'}

#11. Multiple Inputs with Unpacking=Use case: Login form or payment details.
email, password = input("Enter email and password: ").split()                       #Enter email and password: name123 password@123
print("email:", email)                                                              #email: name123
print("password:", password)                                                      #password: password@123  
