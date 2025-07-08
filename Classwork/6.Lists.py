#Lists.py
#Creating Lists
my_list = []
my_list = [1,2,3,4,5,6,7,8,9]
a = [1,2,3,"python",3.14,False]
list_from_tuple = list((1,2,3,4,5,6,7,8,9))
string_to_list = list("python")

#Accessing Elements in a List

#Using Indexing
my_list = ["apple", "banana", "mango", "papaya"]
print(my_list[0]) #apple
print(my_list[2]) #mango
print(my_list[-1]) #papaya

#Using Slicing
my_list = ["apple", "banana", "mango", "papaya"]
print(my_list[0:2]) #['apple', 'banana']
print(my_list[:3]) #['apple', 'banana', 'mango'](from start)
print(my_list[2:]) #['mango', 'papaya'](to end)
print(my_list[::-1]) #['papaya', 'mango', 'banana', 'apple'](Reverse List)

#Modifying Lists
list = [1,2,3,4,5]
list[2] = 19
print(list) #[1, 2, 19, 4, 5](Changing Elements)
list.append(6)
print(list) #[1, 2, 19, 4, 5, 6](adds to the end)
list.insert(1,9)
print(list) #[1, 9, 2, 19, 4, 5, 6](adds at a specific position)
list.extend([13,14,15])
print(list) #[1, 9, 2, 19, 4, 5, 6, 13, 14, 15](adds multiple elememts)
list.remove(13)
print(list) #[1, 9, 2, 19, 4, 5, 6, 14, 15](removes the element)
list.pop(6)
print(list) #[1, 9, 2, 19, 4, 5, 14, 15](removes element at index 6)


#List Methods
numbers = [2,1,3,6,5,2]
print(numbers.count(2)) #2(counts the valur that is repeated)
print(numbers.index(6)) #3(prints the index of the given value)
numbers.sort() #sorts the list in ascending order
print(numbers) #[1, 2, 2, 3, 5, 6]
numbers.reverse()#reverses the list
print(numbers) #[6, 5, 3, 2, 2, 1]
