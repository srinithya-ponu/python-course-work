Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=100
>>> print(type(100)) #<class 'int'>
<class 'int'>
>>> a=1+3j
>>> print(type(a)) #<class 'complex'>
<class 'complex'>
>>> a=5.0
>>> print(type(a)) #<class 'float'>
<class 'float'>
>>> cricketer_name= 'abhishek'
>>> print(type(cricketer_name)) #<class 'str'>
<class 'str'>
>>> cricketer_name= "abhishek
SyntaxError: unterminated string literal (detected at line 1)
>>> cricketer_name= "abhishek"
>>> print(type(cricketer_name)) #<class 'str'>
<class 'str'>
>>> course=['da','ds']
>>> print(type(course)) #<class 'list'>
<class 'list'>
>>> t={1,2,3,4,5}
... t
SyntaxError: multiple statements found while compiling a single statement
>>> t={1,2,3,4,5}
>>> t
{1, 2, 3, 4, 5}
>>> s={1,1,1,1,2,4,3,5,5,5}
>>> s
{1, 2, 3, 4, 5}
>>> print(type(s)) #<class 'set'>
<class 'set'>
>>> randomvar=None
>>> print(type(randomvar)) #<class 'NoneType'>
<class 'NoneType'>
>>> passwordlogin=True
>>> print(type(True)) #<class 'bool'>
<class 'bool'>
