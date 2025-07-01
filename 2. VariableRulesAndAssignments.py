Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> myvar=19
>>> myVar=19
>>> myvar1=19
>>> my_var=19
>>> my@var=19
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> myvar=19
>>> Myvar=19
>>> 1myvar=19
SyntaxError: invalid decimal literal
>>> @myvar=19
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> my var=19
SyntaxError: invalid syntax
>>> myvar= 10
>>> Myvar=1
>>> myvar
10
>>> Myvar
1
>>> a=10
>>> a
10
>>> a,b,c = 1,2,3
>>> a
1
>>> b
2
>>> c
3
>>> a=10
>>> a=199999
>>> a
199999
>>> a,b = 4,6
>>> a,b = b,a
>>> a
6
>>> b
4
del b
b
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b
NameError: name 'b' is not defined
a
6
