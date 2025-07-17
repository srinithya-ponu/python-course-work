#Type Conversion (Type Casting)

#Type conversion in Python refers to converting the value of one data type to another using built-in functions such as int(), float(), str(), bool(), list(), tuple(), set(), and dict().

#1.Coverting from int
int_a=100
print(float(int_a)) #100.0
print(str(int_a))   #'100'
print(bool(int_a))  #True
print(list(int_a))  #TypeError: 'int' object is not iterable
print(set(int_a))   #TypeError: 'int' object is not iterable
print(tuple(int_a)) #TypeError: 'int' object is not iterable
print(dict(int_a))  #TypeError: 'int' object is not iterable


#2.Converting from float
float_a = 4.19
print(int(float_a)) #4
print(str(float_a)) #'4.19'
print(bool(float_a)) #True
print(list(float_a))  #TypeError: 'float' object is not iterable
print(set(float_a))  #TypeError: 'float' object is not iterable
print(tuple(float_a))  #TypeError: 'float' object is not iterable
print(dict(float_a))  #TypeError: 'float' object is not iterable


#3.Converting from string
s = "person"
print(int(s)) #ValueError: invalid literal for int() with base 10: 'person'
s1 = '25'
print(int(s1))  #25
print(float(s))  #ValueError: could not convert string to float: 'person'
print(float(s1))  #25.0
print(list(s))  #['p', 'e', 'r', 's', 'o', 'n']
print(bool(s))  #True
print(tuple(s))  #('p', 'e', 'r', 's', 'o', 'n')
print(set(s))  #{'o', 'e', 'p', 'n', 'r', 's'}
print(dict(s))  #ValueError: dictionary update sequence element #0 has length 1; 2 is required

#4.Converting from list
l = [1,2,3,4,5,6,7,8]
list_a = [1,2,3,4,5,6,7,8]
print(int(list_a))  #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
print(float(list_a))  #TypeError: float() argument must be a string or a real number, not 'list'
print(str(list_a))  #[1, 2, 3, 4, 5, 6, 7, 8]
print(bool(list_a)) #True
print(tuple(list_a)) #(1, 2, 3, 4, 5, 6, 7, 8)
print(set(list_a)) #{1, 2, 3, 4, 5, 6, 7, 8}
print(dict(list_a))  #TypeError: cannot convert dictionary update sequence element #0 to a sequence


#5.Converting from tuple
t = (21,47,29,12)
tuple_c = (21,47,29,12)
print(int(tuple_c)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
print(float(tuple_c))  #TypeError: float() argument must be a string or a real number, not 'tuple'
print(str(tuple_c))  #'(21, 47, 29, 12)'
print(bool(tuple_c))  #True
print(list(tuple_c))  #[21, 47, 29, 12]
print(set(tuple_c))  #{29, 12, 21, 47}
print(dict(tuple_c))  #TypeError: cannot convert dictionary update sequence element #0 to a sequence


#6.Converting from set
a = {1,2,3,4}
set_a = {1,2,3,4}
int(set_a) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(set_a)  #TypeError: float() argument must be a string or a real number, not 'set'
str(set_a)  #'{1, 2, 3, 4}'
bool(set_a)  #True
list(set_a) #[1, 2, 3, 4]
tuple(set_a)  #(1, 2, 3, 4)
dict(set_a)  #TypeError: cannot convert dictionary update sequence element #0 to a sequence


#7.Converting from dict
a = {1:1, 2:8, 3:27}
dict_a = {1:1, 2:8, 3:27}
int(dict_a)  #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(dict_a)#TypeError: float() argument must be a string or a real number, not 'dict'
str(dict_a)  #'{1: 1, 2: 8, 3: 27}'
bool(dict_a) #True
list(dict_a) #[1, 2, 3]
tuple(dict_a) #(1, 2, 3)
set(dict_a) #{1, 2, 3}
     

#8.Converting from bool
a = False
print(int(a))  #0
print(float(a)) #0.0
print(str(a))  #False
print(list(a))  #TypeError: 'bool' object is not iterable
print(tuple(a))  #TypeError: 'bool' object is not iterable
print(set(a))  #TypeError: 'bool' object is not iterable
print(dict(a))  #TypeError: 'bool' object is not iterable
     
b = True
print(int(b))  #1
print(float(b)) #1.0
print(str(b))  #True
print(list(b))  #TypeError: 'bool' object is not iterable
print(tuple(b))  #TypeError: 'bool' object is not iterable
print(set(b))  #TypeError: 'bool' object is not iterable
print(dict(b)) #TypeError: 'bool' object is not iterable     


#9.Dictionary Conversion
d = [('name', 'Arjun'), ('batch', '20'), ('course', 'Datascience')]
print(int(d))  #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
print(float(d)) #TypeError: float() argument must be a string or a real number, not 'list'
print(str(d))  #[('name', 'Arjun'), ('batch', '20'), ('course', 'Datascience')]
print(bool(d))  #True
print(tuple(d))  #(('name', 'Arjun'), ('batch', '20'), ('course', 'Datascience'))
print(set(d))  #{('name', 'Arjun'), ('course', 'Datascience'), ('batch', '20')}
print(set(d))  #{('name', 'Arjun'), ('course', 'Datascience'), ('batch', '20')}
print(list(d)) #[('name', 'Arjun'), ('batch', '20'), ('course', 'Datascience')]     



