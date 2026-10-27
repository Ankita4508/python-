'''
11.Wap to check whether the data is mutable or not.
12.Wap to check whether the given character is digit or not.
13.Wap to check whether the given character is special or not.
14.Wap to check whether a list consists of middle value or not.
15.Wap to check whether the number is even or odd.
16.Wap to check whether the given data is mutable or immutable.
17.Wap to check whether 2 values are pointing to the same memory or not.
18.Consider a tuple of length 2 and check whether the tuple is homogenous or not.
19.Wap to check whether the string is palindrome or not.
20.Wap to check whether the number is positive or negative.

'''
'''
#1
n = eval(input('Enter the data'))
if type(n) in (list, set, dict):
    print('mutable')
else:
    print('immutable')

#2
a = input('Enter the character')
if '0' <= a <='9':
    print('its a digit')
else:
    print('its not a digit')
    
#3
c = input('Enter the character : ')
if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
    print('not a special character')
else:
    print('special character')

#4
l = eval(input('Enter the list : '))
if len(l) % 2 != 0:
    print('has a middle value')
else:
    print('no middle value')

#5
e = int(input('Enter the num'))
if e%2==0 :
    print('even')
else:
    print('odd')

#6
n = eval(input('Enter the data'))
if type(n) in (list, set, dict):
    print('mutable')
else:
    print('immutable')
'''
#7
one = int(input('Enter a num 1: '))
two = int(input('Enter a num 2: '))
if id(one) == id(two):
    print('have same memo')
else:
    print('not have same memo')

#8
tup = eval(input('Enter a tuple: '))
if type(tup[0]) == type(tup[1]):
    print('homogenous')
else:
    print('not homogenous')

#9
p = input('Enter the string:')
q = p[::-1]
if p == q:
    print('palindrome')
else:
    print('not a palindrome')

#10
number = int(input('enter a num'))
if number >= 0:
    print('positive')
else:
    print('negative')
