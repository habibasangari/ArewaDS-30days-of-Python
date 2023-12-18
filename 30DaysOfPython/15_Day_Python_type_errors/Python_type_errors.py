'''print 'hello world'
  File "<stdin>", line 1
    print 'hello world'

PS C:\Users\Admin\Desktop\30DaysOfPython> & "C:/New folder/python.exe" c:/Users/Admin/Desktop/30DaysOfPython/15_Day_Python_type_errors/Python_type_errors.py
  File "c:\Users\Admin\Desktop\30DaysOfPython\15_Day_Python_type_errors\Python_type_errors.py", line 1
    print 'hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?




print(age)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(age)
NameError: name 'age' is not defined




numbers = [1, 2, 3, 4, 5]
numbers[5]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    numbers[5]
IndexError: list index out of range




import maths
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import maths
ModuleNotFoundError: No module named 'maths'



import math
math.PI
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    math.PI
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?



users = {'name':'Asab', 'age':250, 'country':'Finland'}
users['name']
'Asab'
users['county']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    users['county']
KeyError: 'county'



4 + '3'
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    4 + '3'
TypeError: unsupported operand type(s) for +: 'int' and 'str'



from math import power
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    from math import power
ImportError: cannot import name 'power' from 'math' (unknown location)



int('12a')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int('12a')
ValueError: invalid literal for int() with base 10: '12a'



1/0
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero'''
