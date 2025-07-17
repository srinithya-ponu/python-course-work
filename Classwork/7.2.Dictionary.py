#A dictionary in Python is an ordered, mutable collection that stores key-value pairs.
#A dictionary is defined using curly braces {}, where each key is followed by a colon :, and the key-value pairs are separated by commas.
#Syntax of a Dictionary: dictionary_name = {key1: value1, key2: value2, key3: value3}.

#Example of a Dictionary:
student = {
    "name" : "nithya",
    "age" : 21,
    "course" : "ece"
}
print(student)    #{'name': 'nithya', 'age': 21, 'course': 'ece'}

#Dictionary Operations:

#1.Accessing Values:

print(student["name"]) #nithya
print(student.get("age")) #21
print(student.get("section")) #None
print(student["Name"])  #KeyError: 'Name'

#dict[key] will raise a KeyError if the key does not exist.
#dict.get(key, default_value) will return None

#2.Adding and Updating Items:

student["age"] = 22  # Updating existing key
student["city"] = "Hyd"  # Adding a new key-value pair
student["course"] = "DS" # Updating existing key
student["batch no"] = 15 # Adding a new key-value pair
student["inst"] = "codegnan" # Adding a new key-value pair
print(student) #{'name': 'nithya', 'age': 22, 'course': 'DS', 'city': 'Hyd', 'batch no': 15, 'inst': 'codegnan'}

#3.Removing Items from a Dictionary:

#Using pop(key): Removes the specified key and returns its value.
age = student.pop("age")
print(student)  #{'name': 'nithya', 'course': 'DS', 'city': 'Hyd', 'batch no': 15, 'inst': 'codegnan'}

#Using del: Deletes a specific key-value pair or the entire dictionary.
del student["course"]
print(student) #{'name': 'nithya', 'city': 'Hyd', 'batch no': 15, 'inst': 'codegnan'}

#Using popitem(): Removes and returns the last inserted key-value pair.
student.popitem() #('inst', 'codegnan')
print(student) #{'name': 'nithya', 'city': 'Hyd', 'batch no': 15}

#Using clear(): Removes all key-value pairs, making the dictionary empty.
student.clear()
print(student)  #{}

#Dictionary Built-in methods

#1. Dictionary Methods for Accessing Data
person = {'name':'nithya','id':'419','course':'Ds','batch':'15','branch':'ECE'}

#dict.get(key,default)=Returns the value for the given key; returns default if key is not found
print(person.get("name"))        #nithya
print(person.get("branch"))      #ECE
print(person.get("age"))         #None

#dict.keys()=Returns a view object containing all keys
print(person.keys())             #dict_keys(['name', 'id', 'course', 'batch', 'branch']) 
print(list(person.keys()))       #['name', 'id', 'course', 'batch', 'branch']

#dict.values()=Returns a view object containing all values
print(person.values())  #dict_values(['nithya', '419', 'Ds', '15', 'ECE'])
print(list(person.values()))  #['nithya', '419', 'Ds', '15', 'ECE']
 
#dict.items()= Returns a view object containing all key-value pairs as tuples
print(person.items())        #dict_items([('name', 'nithya'), ('id', '419'), ('course', 'Ds'), ('batch', '15'), ('branch', 'ECE')])

#2. Dictionary Methods for Adding and Updating Data

person = {'name':'nithya','id':'419','course':'Ds','batch':'15','branch':'ECE'}
print("before:",person)    #before: {'name': 'nithya', 'id': '419', 'course': 'Ds', 'batch': '15', 'branch': 'ECE'}                         
person.update({"state":"Telangana"})  
print("After:",person)   #After: {'name': 'nithya', 'id': '419', 'course': 'Ds', 'batch': '15', 'branch': 'ECE', 'state': 'Telangana'}                        
print(person.setdefault("city", "unknown"))
print(person)   #{'name': 'nithya', 'id': '419', 'course': 'Ds', 'batch': '15', 'branch': 'ECE', 'state': 'Telangana', 'city': 'unknown'}

#3. Dictionary Methods for Removing Data

#dict.pop(key,default)=Removes and returns value of the specified key
person = {'name':'nithya','id':'419','course':'Ds','batch':'15','branch':'ECE'}
val = person.pop('course')
print(val)   #Ds           
print(person) #{'name': 'nithya', 'id': '419', 'batch': '15', 'branch': 'ECE', 'state': 'Telangana', 'city': 'unknown'}

val = person.pop('id')
print(val)  #419
print(person)  #{'name': 'nithya', 'batch': '15', 'branch': 'ECE', 'state': 'Telangana', 'city': 'unknown'}              

#dict.popitem()=Removes and returns the last inserted key-value pair
person = {'name':'nithya','id':'419','course':'Ds','batch':'15','branch':'ECE'}
person.popitem()  #('city', 'unknown')
print(person)   #{'name': 'nithya', 'batch': '15', 'branch': 'ECE', 'state': 'Telangana'}                 

#dict.clear() Removes all key-value pairs, making the dictionary empty
person = {'name':'nithya','id':'419','course':'Ds','batch':'15','branch':'ECE'}
person.clear()
print(person)    #{}

#del dict[key]= Deletes a specific key from the dictionary
data = {'a':10, 'b':20, 'c':30}
del data['b']
print(data)                               #{'a': 10, 'c': 30}

#Built-in Functions for Dictionaries=Python provides several built-in functions that can be used with dictionaries.

#1. len(dict)=Returns the number of items in the dictionary
person = {'name':'nithya','id':'419','course':'Ds','batch':'15','branch':'ECE'}
print(len(person))                     #5

#2. Max
print(max(person))                     #state

#3. Min
print(min(person))                     #batch

#4. Sorted()
print(sorted(person))                  #['batch', 'branch', 'name', 'state']

#Nested Dictionaries=A dictionary can contain another dictionary as its value.

child1 = {"name": "jerry", "year": 2004}
child2 = {"name": "Tom", "year": 2007}
myfamily = {"child1": child1, "child2": child2}
print(myfamily["child2"]["name"])                           #Tom
print(myfamily["child1"]["year"])                           #2004

#Dictionary Comprehension=You can create dictionaries dynamically using dictionary comprehension.

squares = {n: n*n for n in range(1, 8)}
print(squares)                                     #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}








