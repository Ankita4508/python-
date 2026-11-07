#1. Write a Python program to perform a general copy on a list. Modify the original
#list and display both the original and copied variables.

a = [1,2.2,3+4j,'ankita',['aadi',44]]
b=a
a[2]=55
print(a)
print(b)

#2. Write a Python program to perform a general copy on a nested list.Modify
#both the outer list and the nested list, then display the changes in bothvariables.

print(a)
a[1]=11
a[-1][-1]=11
print(a)
print(b)

#3. Write a Python program to perform a shallow copy using the copy() method. Modify an
#outer element in the original list and display both lists.

c=[1,2.2,3+4j,'ankita',['aadi',44]]
d=c.copy()
c[0]=1000
c[-1][0]=500
print(c)
print(d)


#4. Write a Python program to perform a shallow copy on a nested list. Modify an element
#inside the nested list and display both the original and copied lists.

c=[1,2.2,3+4j,'ankita',['aadi',44]]
d=c.copy()
c[0]=1000
c[-1][0]=500
print(c)
print(d)

#5. Write a Python program to perform a shallow copy on a nested list. Modify one outer
#element and one nested element. Display both lists.

c=[1,2.2,3+4j,'ankita',['aadi',44]]
d=c.copy()
c[0]=1000
c[-1][0]=500
print(c)
print(d)

#6. Write a Python program to perform a deep copy using the deepcopy() method from the
#copy module. Modify an outer element in the original list and display both lists.
import copy
e=[1,2.2,3+4j,'ankita',['aadi',44]]
f=copy.deepcopy(e)
e[1]=300
e[-1][1]=600
print(e)
print(f)

#7. Write a Python program to perform a deep copy on a nested list. Modify an element
#inside the nested list in the original list and display both lists.

import copy
e=[1,2.2,3+4j,'ankita',['aadi',44]]
f=copy.deepcopy(e)
e[1]=300
e[-1][1]=600
print(e)
print(f)

#8. Write a Python program to create general, shallow, and deep copies of the same nested
#list. Modify an outer element in the original list and display all four lists

l=[11,22,33,44,55.5,['ankita','aadesh']]
z=l
print(z)
print(l)
l[0]=111
l[-1][-1]='smita'
print(z)
print(l)
y=l.copy()
l[1]=4000
l[-1][0]=500
print(l)
print(y)
x=copy.deepcopy(l)
l[0]=100
l[-1][-1]=100
print(l)
print(x)

#9. Write a Python program to create general, shallow, and deep copies of a nested list.
#Modify a nested element in the original list and display all four lists.

l=[11,22,33,44,55.5,['ankita','aadesh']]
z=l
print(z)
print(l)
l[0]=111
l[-1][-1]='smita'
print(z)
print(l)
y=l.copy()
l[1]=4000
l[-1][0]=500
print(l)
print(y)
x=copy.deepcopy(l)
l[0]=100
l[-1][-1]=100
print(l)
print(x)

#10. Write a Python program to create general, shallow, and deep copies of a nested list.
#Modify both outer and nested elements in the original list. Display all four lists and
#compare their IDs using id().

l=[11,22,33,44,55.5,['ankita','aadesh']]
z=l
print(z)
print(l)
l[0]=111
l[-1][-1]='smita'
print(z)
print(l)
print(id(l))
print(id(z))
y=l.copy()
l[1]=4000
l[-1][0]=500
print(l)
print(y)
print(id(l))
print(id(y))
x=copy.deepcopy(l)
l[0]=100
l[-1][-1]=100
print(l)
print(x)
print(id(l))
print(id(x))


