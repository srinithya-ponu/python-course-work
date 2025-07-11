#Tuples.py
t = (1,3,5,7,9,"apple","mango", "papaya")
type (t) #<class 'tuple'>

#Accessing Tuple Elements

#Indexing(tuple[index])
t
(1, 3, 5, 7, 9, 'apple', 'mango', 'papaya')
print(t[3]) #7
print(t[6]) #mango
#Negative Indexing
t
(1, 3, 5, 7, 9, 'apple', 'mango', 'papaya')
print(t[-3]) #apple
#Slicing(tuple[start:end])
t
(1, 3, 5, 7, 9, 'apple', 'mango', 'papaya')
print(t[2:5]) #(5, 7, 9)
print(t[5:8]) #('apple', 'mango', 'papaya')

#Operations on Tuples

#Concatenation
t1 = (10,20)
t2 = ("apple", "banana")
new_t = t1+t2
print(new_t) #(10, 20, 'apple', 'banana')
#Repetition
new_t
(10, 20, 'apple', 'banana')
print(new_t * 2) #(10, 20, 'apple', 'banana', 10, 20, 'apple', 'banana')
#Membership Testing
new_t
(10, 20, 'apple', 'banana')
print("apple" in new_t) #True
print(30 in new_t) #False
print("payaya" not in new_t) #True
#Tuple Unpacking
new_t
(10, 20, 'apple', 'banana')
a, b, c, d = new_t
print(a, b, c, d) #10 20 apple banana

#Tuple Methods & Built-in Functions for Tuples
t = (1,2,2,3,3,3,5,6)
print(t.count(3)) #3
print(t.index(3)) #3
print(len(t)) #8
print(max(t)) #6
print(min(t)) #1
print(sum(t)) #25
