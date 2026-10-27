Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#que1
s = {10,20,30,20,10,40}
type(s)
<class 'set'>
len(s)
4
#que 2
a = {'apple',10,True,5,10}
a
{True, 'apple', 10, 5}
len(s)
4
#que 3
set()
set()
e = ()
e
()
dict = {}
dict
{}
type(e)
<class 'tuple'>
type(dict)
<class 'dict'>
bool(e)
False
bool(dict)
False
#que 5
ad =  {'red', 'blue', 'green', 'yellow'}
ad
{'red', 'green', 'blue', 'yellow'}
ad.remove('green')
ad
{'red', 'blue', 'yellow'}
#que 4
b = {10, 20, 30, 40}
b
{40, 10, 20, 30}
b.add(50)
b.add('Python')
b
{'Python', 40, 10, 50, 20, 30}
c = {100, 200, 300, 400}
c
{400, 100, 300, 200}
c.pop()
400
c
{100, 300, 200}
#que 7
f = (4,'ankita',[56,'aadi'],(5,99))
f
(4, 'ankita', [56, 'aadi'], (5, 99))
type(f)
<class 'tuple'>
f{4,'ankita',[56,'aadi'],(5,99)}
SyntaxError: invalid syntax
f = {4,'ankita',[56,'aadi'],(5,99)}
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    f = {4,'ankita',[56,'aadi'],(5,99)}
TypeError: unhashable type: 'list'
#we cant use the list in the set cause list is mutable and therfore unhashable
#que 8
g =  {1, 2, 3, 4, 5}
g
{1, 2, 3, 4, 5}
g[1]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    g[1]
TypeError: 'set' object is not subscriptable
#que 9
h = {10, 20, 30}
h
{10, 20, 30}
h.add(20)
h.add(40)
h
{40, 10, 20, 30}
len(h)
4
#que 9
#que 10
i =  {'name': 'Sam', 'age': 21, 'marks': 85}
i
{'name': 'Sam', 'age': 21, 'marks': 85}
type(i)
<class 'dict'>
len(d)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    len(d)
NameError: name 'd' is not defined. Did you mean: 'ad'?
len(i)
3
#que 11
j = {'stud_id' : 101, 'name':'ravi','marks':90}
j
{'stud_id': 101, 'name': 'ravi', 'marks': 90}
j.add('city':'Pune')
SyntaxError: invalid syntax
j.add{'city':'Pune'}
SyntaxError: invalid syntax
j['city']='Pune'
j
{'stud_id': 101, 'name': 'ravi', 'marks': 90, 'city': 'Pune'}
#que 12
k = {'a': 10, 'b': 20, 'c': 30}
k
{'a': 10, 'b': 20, 'c': 30}
k[b]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    k[b]
TypeError: unhashable type: 'set'
k['b']
20
#que 13
l = {'Maths': 80, 'Science': 75, 'English': 90}
l
{'Maths': 80, 'Science': 75, 'English': 90}
l['Science']=85
l
{'Maths': 80, 'Science': 85, 'English': 90}
#que 14
m = {1: 'one', 2: 'two', 3: 'three'}
m
{1: 'one', 2: 'two', 3: 'three'}
d.pop(2)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    d.pop(2)
NameError: name 'd' is not defined. Did you mean: 'ad'?
m.pop(2)
'two'
m
{1: 'one', 3: 'three'}
#que 15
n =  {'name': 'Amit', 'age': 22, 'city': 'Mumbai'}
n
{'name': 'Amit', 'age': 22, 'city': 'Mumbai'}
n.keys
<built-in method keys of dict object at 0x000001B9C35DBB40>
9
n.keys()
dict_keys(['name', 'age', 'city'])
n.values()
dict_values(['Amit', 22, 'Mumbai'])
n.items()
dict_items([('name', 'Amit'), ('age', 22), ('city', 'Mumbai')])
#que 16
o = {10: 100, 20: 200, 30: 300}
o
{10: 100, 20: 200, 30: 300}
o[40]=400
o
{10: 100, 20: 200, 30: 300, 40: 400}
o[10]=500
o
{10: 500, 20: 200, 30: 300, 40: 400}
#que 17
p = {12:13,'name':'ankita',(14,89):(89,678)}
p
{12: 13, 'name': 'ankita', (14, 89): (89, 678)}
#que 18
>>> q = {'x': 10, 'y': 20, 'z': 30}
>>> q['a']
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    q['a']
KeyError: 'a'
>>> #que 19
>>> r =  {1: 10, 2: 20, 3: 30}
>>> r
{1: 10, 2: 20, 3: 30}
>>> len(r)
3
>>> r[4]=40
>>> r
{1: 10, 2: 20, 3: 30, 4: 40}
>>> len(r)
4
>>> #que 20
>>> t =  {'Python': 3, 'Java': 2, 'C++': 1}
>>> t
{'Python': 3, 'Java': 2, 'C++': 1}
>>> t['Java']=5
>>> t
{'Python': 3, 'Java': 5, 'C++': 1}
>>> t.remove('C++')
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    t.remove('C++')
AttributeError: 'dict' object has no attribute 'remove'
>>> t.remove['C++']
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    t.remove['C++']
AttributeError: 'dict' object has no attribute 'remove'
>>> t.pop['C++']
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    t.pop['C++']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> t.pop('C++')
1
>>> t
{'Python': 3, 'Java': 5}
>>> t.keys()
dict_keys(['Python', 'Java'])
>>> t.values()
dict_values([3, 5])
>>> t.items()
dict_items([('Python', 3), ('Java', 5)])
