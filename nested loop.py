#1. Write a Python program to print each character of every word in the following list using nested `for` loops.
# ```python
'''
words = ['apple', 'ball', 'cat']
for i in words:
    for j in i:
        print(j, end='  ')
    print()
    
#2. Write a Python program to count the total number of vowels present in each word using nested `for` loops.
#   ```python
words = ['apple', 'banana', 'grapes']
for i in words:
    c = 0
    for j in i:
        if j in 'AEIOUaeiou':
            c+=1
    print(i, ':',c)



#3. Write a Python program to find and print all common elements between two lists using nested `for` loops.
#   ```python
a = [10, 20, 30, 40]
b = [20, 40, 50, 60]
for i in a:
    for j in b:
        if i==j:
            print(i)

#4. Write a Python program to print all possible pairs of elements from two lists using nested `for` loops.
 #  ```python
a = [1, 2, 3]
b = [4, 5]
for i in a:
    for j in b:
        print(i,j)

#5. Write a Python program to count the total number of even numbers present in a nested list using nested `for` loops.
#   ```python
a = [[10, 15, 20], [25, 30, 35], [40, 45, 50]]
c = 0
for i in a:
    for j in i:
        if j%2==0:
            c+=1
print(c)

'''

'''
1)

*****
*****
*****
*****
*****
'''
n=5
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()
'''
2)

*****
*   *
*   *
*   *
*****
'''
n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end='')
        else:
            print(' ', end='')
    print()
'''

3)

*
**  
* * 
*  *
*****
'''
n=5
for i in range(n):
    for j in range(i):
        print(
'''

4)

    *
   ** 
  * *
 *  *
*****
'''
