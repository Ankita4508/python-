'''
for i in 'ankita':
    print(i)

for i in [1,2,3,4]:
    print(i)

for i in (1,2,3,4):
    print(i)

for i in {1,2,3,4}:
    print(i)

for i in {'a':1,'b':2}:
    print(i)

for i in range(1,6):
    print(i)

#71.Wap to print all the integers present in a list.
for i in [1,2,3,4,'ankita']:
    if type(i) == int:
        print(i)
    
#72.Wap to find the length of homogenous tuple without len().
length = 0
for i in (1,2,3,4,5,5,6,7,8,9,90):
    length += 1
print(length)

#73.Wap to extract all the even numbers present in a list.
for i in [1,2,3,4,5,6,7,8,9]:
    if i%2==0:
        print(i)
    
#74.Wap to remove duplicates from list
    
o=[]
for i in [1,2,3,4,5,3,5,5,3]:
    if i not in o:
        o = o + [i]
print(o)

#75.Wap to reverse a string without using slicing.
s = 'ankita'
r = ''
for i in s:
    r = i+r
print(r)
    
#76.wap to extract all the lowercase characters in a string only if the ascii value is
#even.
for i in 'ankita':
    if 'a' <=i <= 'z':
        if ord(i)%2==0:
            print(i)
        
#77.Wap to check whether the last digit of an integer is even or not.
for i in [123,345,678]:
    l = i%10
    if l%2==0:
        print(i,'Even')
    else:
        print(i,'odd')
'''

#78.Wap to extract all the key value pairs from the dictionary only if the keys are of
#string datatype and values are integers.
d = {'a':1,'b':3,23:'snk'}
for i in d:
    if type(i) == str and type(d[i])==int:
        print(i, d[i])

    
#79.Wap to extract key value pairs from the dictionary only if both keys and values
#are exactly same.
d = {'a': 'a', 'b': 3, 23: 23, 'x': 'y'}
o={}
for i in d:
    if i==d[i]:
        o[i]=d[i]
        
print(o)

#80.Wap to get the following output using len function.
#S=’power star’
#Out={‘power’:5,’star’:4}
s = 'power star'
l=s.split()
d={}
for i in l:
    d[i]=len(i)

print(d)
