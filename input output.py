Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a ='ankita'
>>> print('ankita','aadi')
ankita aadi
>>> print('ankita','aadesh',sep='  ',end='\n')
ankita  aadesh
>>> print('anku','aadu')
anku aadu
>>> a = int(input('enter the age : ')
...         21
...         
SyntaxError: '(' was never closed
>>> a=int(input('Enter the age : '))
...         
Enter the age : 21
>>> a=eval(input('enter the list: '))
...         
enter the list: [1,2,3,4]
>>> print(a)
...         
[1, 2, 3, 4]
>>> type(a)
...         
<class 'list'>
>>> 
>>> name = int(input('Enter your Name : '))
...         
Enter your Name : Ankita
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name = int(input('Enter your Name : '))
ValueError: invalid literal for int() with base 10: 'Ankita'
>>> name = input('Enter your name : ')
...         
Enter your name : Ankita
>>> age = int(input('Enter your age : '))
...         
Enter your age : 21
>>> w = eval(input('Enter your weight : '))
...         
Enter your weight : 58
>>> a = eval(input('Enter a num 1 : '))
...         
Enter a num 1 : 12
>>> b = eval(input('Enter a num 2 : '))
...         
Enter a num 2 : 23
>>> list = eval(input('Enter the list : '))
        
Enter the list : [1,2,3,4]
marks = eval(input('Enter the marks in tuple :))
                   
SyntaxError: unterminated string literal (detected at line 1)
marks = eval(input('Enter the marks in tuple : '))
                   
Enter the marks in tuple : (87,99,96)
print(name,age,sep='*****')
                   
Ankita*****21
print('weight: ',w)
                   
weight:  58
print('name datatype:'type(name))
                   
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('name datatype:',type(name))
                   
name datatype: <class 'str'>
print('name datatype:',type(age))
                   
name datatype: <class 'int'>
print('List:',list)
                   
List: [1, 2, 3, 4]
print('tuple:',marks)
                   
tuple: (87, 99, 96)
print('sum of two numbers are:',a+b,sep=' ',end='-----Program completed')
                   
sum of two numbers are: 35-----Program completed
