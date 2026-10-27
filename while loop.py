#1
'''
i = 1
while i<6:
    print('python')
    i+=1
#20.Wap to print n natural numbers.
n = int(input('enter a num'))
i=1
while i<=n:
    print(i)
    i+=1
    
#41.Wap to print multiplication table for n.
a = int(input('enter a number for table'))
i = 1
while i<=10:
    print(i*a)
    i+=1
    
#42.Wap to find the sum of n natural numbers.
b = int(input('enter a number for sum of n'))
i=1
sum = 0
while i<=b:
    sum = sum + i
    i+=1
print(sum)

#43. Wap to find the product of n natural numbers or factorial of a number.
c = int(input('enter a number for product of n or factorial'))
i = 1
fact = 1
while i<=n:
    fact= fact* i
    i+=1
print(fact)

'''

''' 
#Wap to print all the characters of a string.
s = input('enter a string')
i=0
while i<len(s):
    print(s[i])
    i+=1
    
#Wap to print all the characters present at even index of a string.
a = input('enter a string')
i =0
while i < len(s):
    if i%2==0:
        print(s[i])
    i+=1
        
#Wap to extract all the lowercase characters present in a string.
b = input('enter a string')
i=0
while i< len(s):
    if 'a' <= s[i] <= 'z':
        print(s[i])
    i+=1
#Wap to extract all the vowels present in a string.
c = input('enter a string')
i=0
while i<len(s):
    if s[i] in ('a','e','o','u','i','A','E','I','O','U'):
        print(s[i])
    i+=1

'''
#Wap to reverse the given number.
n = int(input('enter a number'))
rev = 0
while n>0:
    l = n%10
    rev = rev*10+l
    n = n//10
print(rev)

#Wap to remove duplicates from a list without converting into set.
a = eval(input('enter a list'))
o=[]
i = 0
while i< len(a):
    if a[i] not in o:
        o +=[a[i]]
    i+=1
print(o)
