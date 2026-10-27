Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = ['ankita','aadesh',19,55.6]
a
['ankita', 'aadesh', 19, 55.6]
id(a)
2500880765120
bool(a)
True
type(a)
<class 'list'>
len(a)
4
a[1]
'aadesh'
a[-1]
55.6
a[-2]
19
a[0]
'ankita'
a[0][2]
'k'
a[0][-1]
'a'
a.append('satara')
a
['ankita', 'aadesh', 19, 55.6, 'satara']
a.extend([50,456,253,'kbpcoes'])
a
['ankita', 'aadesh', 19, 55.6, 'satara', 50, 456, 253, 'kbpcoes']
a.insert(5,10000
        
KeyboardInterrupt
a.insert(5,10000)
         
a
         
['ankita', 'aadesh', 19, 55.6, 'satara', 10000, 50, 456, 253, 'kbpcoes']
a.pop
         
<built-in method pop of list object at 0x00000246481C10C0>
a.pop()
         
'kbpcoes'
a
         
['ankita', 'aadesh', 19, 55.6, 'satara', 10000, 50, 456, 253]
a.pop()
         
253
a
         
['ankita', 'aadesh', 19, 55.6, 'satara', 10000, 50, 456]
a.remove(50)
         
a
         
['ankita', 'aadesh', 19, 55.6, 'satara', 10000, 456]
a[-1]=5+2j
         
a
         
['ankita', 'aadesh', 19, 55.6, 'satara', 10000, (5+2j)]
b=(11,12,13,14)
         
b
         
(11, 12, 13, 14)
>>> t=(11,true,(5+3j),'ank')
...          
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    t=(11,true,(5+3j),'ank')
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> t=(11,True,(5+3j),'ankita')
...          
>>> t
...          
(11, True, (5+3j), 'ankita')
>>> id(t)
...          
2500880879264
>>> type(t)
...          
<class 'tuple'>
>>> tuple()
...          
()
>>> bool(t)
...          
True
>>> len(t)
...          
4
>>> t[1]
...          
True
>>> t[0]
...          
11
>>> t[-1]
...          
'ankita'
>>> t[-1][3]
...          
'i'
