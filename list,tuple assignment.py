Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1. Create a list containing five integers. Print the list, its data type, length, and Boolean value.
SyntaxError: invalid syntax
a = [1,2,3,4,5]
s
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s
NameError: name 's' is not defined
a
[1, 2, 3, 4, 5]
len(a)
5
type(a)
<class 'list'>
bool(a)
True

2. Create a heterogeneous list containing an integer, a float, a Boolean, a string, and a complex number. Print each element using positive indexing.
SyntaxError: invalid syntax
b
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b
NameError: name 'b' is not defined
b
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b
NameError: name 'b' is not defined
b = [1,2.3,'ankita',4+21j,True]
b
[1, 2.3, 'ankita', (4+21j), True]
print(b[0],b[1],b[2],b[3],b[4]]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
print(b[0],b[1],b[2],b[3],b[4])
1 2.3 ankita (4+21j) True

3. Create a list of six student names. Print the first, third, and last names using positive and negative indexing.
SyntaxError: invalid syntax
c = ['ankita', 'aadesh', 'riya','ravi','parth','neha']
c
['ankita', 'aadesh', 'riya', 'ravi', 'parth', 'neha']
print(c[0],c[2],c[-1])
ankita riya neha

4. Create a list containing `['Python', 'Java', 'SQL', 'HTML']`. Print the second character of the first element and the last character of the third element.
SyntaxError: invalid syntax
d = ['Python', 'Java', 'SQL', 'HTML']
d
['Python', 'Java', 'SQL', 'HTML']
print(d[0][1], d[2][-1])
y L

5. Create a list containing `[10, 20, 30, 40, 50]`. Add `60` at the end using `append()` and display the updated list.
SyntaxError: invalid syntax
e = [10, 20, 30, 40, 50]
e
[10, 20, 30, 40, 50]
e.append(60)
e
[10, 20, 30, 40, 50, 60]

6. Create a list of three product prices. Add four new prices at the end using `extend()` and display the result.
SyntaxError: invalid syntax
f = [200,300,400]
f
[200, 300, 400]
f.extend([2000,4000,3400,234])
f
[200, 300, 400, 2000, 4000, 3400, 234]

7. Create a list containing `['Monday', 'Tuesday', 'Thursday', 'Friday']`. Insert `'Wednesday'` at index `2` and display the updated list.
SyntaxError: invalid syntax

g = ['Monday', 'Tuesday', 'Thursday', 'Friday']
g
['Monday', 'Tuesday', 'Thursday', 'Friday']
g.insert(2,'Wendesday')
g
['Monday', 'Tuesday', 'Wendesday', 'Thursday', 'Friday']

8. Create a list containing `[12, 24, 36, 48, 60]`. Remove the last element using `pop()` and print both the removed element and the updated list.


SyntaxError: invalid syntax
h = [12, 24, 36, 48, 60]
g
['Monday', 'Tuesday', 'Wendesday', 'Thursday', 'Friday']
h
[12, 24, 36, 48, 60]
h.pop()
60
h.pop()
48
h
[12, 24, 36]
9. Create a list containing `['red', 'blue', 'green', 'blue', 'yellow']`. Remove the first occurrence of `'blue'` using `remove()` and display the list.
SyntaxError: invalid syntax
i = ['red', 'blue', 'green', 'blue', 'yellow']
i
['red', 'blue', 'green', 'blue', 'yellow']
i.remove('blue')
i
['red', 'green', 'blue', 'yellow']

10. Create a list containing `[100, 200, 300, 400, 500]`. Replace the value at index `2` with `999` and display the updated list.
SyntaxError: invalid syntax

j = [100, 200, 300, 400, 500]
j
[100, 200, 300, 400, 500]
j[2]=999
j
[100, 200, 999, 400, 500]

11. Create a list containing `[10, True, 'Python', 5.5, 'Data']`. Replace `True` with `False` using indexing and display the updated list.
SyntaxError: invalid syntax

k = [10, True, 'Python', 5.5, 'Data']
k
[10, True, 'Python', 5.5, 'Data']
k['True']= False
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    k['True']= False
TypeError: list indices must be integers or slices, not str
k[1]='False'
k
[10, 'False', 'Python', 5.5, 'Data']
k['True']='False'
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    k['True']='False'
TypeError: list indices must be integers or slices, not str

12. Create a list containing `['pen', 'pencil', 'eraser']`. Add `'sharpener'` using `append()`, then add `['scale', 'marker']` using `extend()`. Display the final list.
SyntaxError: invalid syntax

l = ['pen', 'pencil', 'eraser']
l
['pen', 'pencil', 'eraser']
>>> l.append('sharpener')
>>> l.extends(['scale','marker'])
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    l.extends(['scale','marker'])
AttributeError: 'list' object has no attribute 'extends'. Did you mean: 'extend'?
>>> l.extend(['scale','marker'])
>>> l
['pen', 'pencil', 'eraser', 'sharpener', 'scale', 'marker']
>>> 
>>> 13. Create a list containing `[11, 22, 33, 44, 55, 66]`. Remove the last two elements using two `pop()` operations and display the final list.
SyntaxError: invalid syntax
>>> 
>>> m = [11, 22, 33, 44, 55, 66]
>>> m
[11, 22, 33, 44, 55, 66]
>>> m.pop()
66
>>> m.pop()
55
>>> m
[11, 22, 33, 44]
>>> 
>>> 14. Create a list containing `['apple', 'banana', 'cherry', 'banana', 'mango']`. Remove `'banana'` twice using `remove()` and display the updated list.
SyntaxError: invalid syntax
>>> 
>>> n = ['apple', 'banana', 'cherry', 'banana', 'mango']
>>> n
['apple', 'banana', 'cherry', 'banana', 'mango']
>>> n.remove('banana')
>>> n
['apple', 'cherry', 'banana', 'mango']
>>> n.remove('banana')
>>> n
['apple', 'cherry', 'mango']
>>> 
>>> 15. Create a list containing `[5, 10, 15, 20]`. Insert `7` at index `1`, append `25`, and extend the list with `[30, 35]`. Display the final list.
SyntaxError: invalid syntax
>>> 
>>> o = [5, 10, 15, 20]
>>> o
[5, 10, 15, 20]
>>> o[1]=7
>>> o.append(25)
>>> o.extend([30,35])
>>> o
[5, 7, 15, 20, 25, 30, 35]
>>> 
>>> 16. Create a nested list `[['Sam', 21], ['Raj', 23], ['Priya', 22]]`. Print `'Sam'`, `23`, and `'Priya'` using nested indexing.
SyntaxError: invalid syntax

p = [['Sam', 21], ['Raj', 23], ['Priya', 22]]
p
[['Sam', 21], ['Raj', 23], ['Priya', 22]]
print(p[0][0],p[1][1],p[-1][0])
Sam 23 Priya

17. Create a list containing `['Python', 'Programming', 'Language']`. Print the second character of each string using nested indexing.
SyntaxError: invalid syntax
q = ['Python', 'Programming', 'Language']
q
['Python', 'Programming', 'Language']
print(q[0][1],q[1][1],q[2][1])
y r a

18. Create a list containing `[10, 20, 30, 40, 50]`. Print the element at index `1`, the element at index `-2`, and the last element.
SyntaxError: invalid syntax

r = [10, 20, 30, 40, 50]
print(r[1],p[-2],p[-1])
20 ['Raj', 23] ['Priya', 22]
print(r[2],r[-2],r[-1])
30 40 50
r
[10, 20, 30, 40, 50]

19. Create a list containing `[1, 2, 3]`. Append the list `[4, 5]` and display the result. Then create another list and use `extend([4, 5])`. Display both lists and observe the difference.
SyntaxError: invalid syntax

s = [1, 2, 3]
s
[1, 2, 3]
s.append([4,5])
s
[1, 2, 3, [4, 5]]
s.extend([4,5])
s
[1, 2, 3, [4, 5], 4, 5]

20. Create a list containing `[10, 20, 30, 40, 50]`. Remove the value `30`, replace the value `40` with `400`, and append `60`. Display the final list.
SyntaxError: invalid syntax

t = [10, 20, 30, 40, 50]
t.remove(30)
t
[10, 20, 40, 50]
t[40]=400
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    t[40]=400
IndexError: list assignment index out of range
t[-2]=400
t
[10, 20, 400, 50]
t.append(60)
t
[10, 20, 400, 50, 60]

21. Create a tuple containing five integers. Print the tuple, its data type, length, and Boolean value.
SyntaxError: invalid syntax

u = (1,2,3,4,5)
u
(1, 2, 3, 4, 5)
type(u)
<class 'tuple'>
len(u)
5
bool(u)
True

22. Create a heterogeneous tuple containing an integer, a Boolean, a complex number, and a string. Print each element using positive indexing.
SyntaxError: invalid syntax

v = (1,2.2,True, 'ankita',34+8j)
print(v[0],v[1],v[2],v[3],v[4])
1 2.2 True ankita (34+8j)

23. Create a tuple containing `('Python', 'Java', 'C++', 'SQL')`. Print the first element, the last element, and the last character of the last element.
SyntaxError: invalid syntax

x = ('Python', 'Java', 'C++', 'SQL')
x
('Python', 'Java', 'C++', 'SQL')
print(x[0],x[-1],x[-1][-1])
Python SQL L

24. Create a tuple containing `(10, True, 'Sam', 5.5, 'Python')`. Print the third element using positive indexing and the same element using negative indexing.
SyntaxError: invalid syntax

y = (10, True, 'Sam', 5.5, 'Python')
y
(10, True, 'Sam', 5.5, 'Python')
print(y[2],y[-3])
Sam Sam

25. Create a tuple containing `('red', 'green', 'blue')` and a list containing the same values. Attempt to replace `'green'` with `'yellow'` in both. Observe and explain why the operations behave differently.
SyntaxError: invalid syntax

z = ('red', 'green', 'blue')
z[1]='yellow'
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    z[1]='yellow'
TypeError: 'tuple' object does not support item assignment
this error happes cause tuple is immutable it cant be change modify update delete or add the values
SyntaxError: invalid syntax
