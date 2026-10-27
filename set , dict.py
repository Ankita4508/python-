Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = {'ankita',1,True,8+9j}
s
{1, 'ankita', (8+9j)}
id(s)
1572567558944
type(S)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined. Did you mean: 's'?
type(s)
<class 'set'>
set()
set()
>>> bool(s)
True
>>> len(s)
3
>>> s.add(15+5j)
>>> s
{1, 'ankita', (8+9j), (15+5j)}
>>> s.pop()
1
>>> s
{'ankita', (8+9j), (15+5j)}
>>> s.remove('ankita')
>>> s
{(8+9j), (15+5j)}
>>> #dictionary
>>> d = {1:2,3:4}
>>> d
{1: 2, 3: 4}
>>> id(d)
1572573133312
>>> type(d)
<class 'dict'>
>>> dict()
{}
>>> bool(d)
True
>>> len(d)
2
>>> d
{1: 2, 3: 4}
>>> d[7]=8
>>> d
{1: 2, 3: 4, 7: 8}
>>> d[1]
2
>>> d[1]=100
>>> d
{1: 100, 3: 4, 7: 8}
>>> d.pop(3)
4
>>> d
{1: 100, 7: 8}
>>> d.keys()
dict_keys([1, 7])
>>> d.values()
dict_values([100, 8])
>>> d.items()
dict_items([(1, 100), (7, 8)])
