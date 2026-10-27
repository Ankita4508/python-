#21. Wap to check whether the char is uppercase, lowercase, digit or special char.
'''
a = input('enter a character')
if 'a' <= a <= 'z':
    print('lowercase')
elif 'A' <= a <= 'Z':
    print('uppercase')
elif '0' <= a <= '9':
    print('digit')
else:
    print('special char')


#22. Wap to check whether the given integer is single digit or two digits or three
#digits or more than three digits.
n=int(input('Enter the number:'))
if 0<=n<=9:
    print('1 digit')
elif 10<=n<=99:
    print('2 digit')
else:
    print('more than 2 digit')
    

#23.Wap to check the given points are lying in which quadrant.
x = int(input('enter x:'))
y = int(input('enter y:'))

if x>0 and y>0:
    print('first quadrant')
elif x<0 and y >0:
    print('second quadrant')
elif x<0 and y<0:
    print('third quadrant')
elif x>0 and y <0:
    print('fourth quadrant')
elif x == 0 and y==0:
    print('origin')
elif y==0:
    print('on the x-axis')
else:
    print('on y axis')
    
#24. Wap to find the greatest of 3 numbers.
aa = int(input('enter a num1'))
b = int(input('enter a num2'))
c = int(input('enter a num3'))
if aa >= b and aa >= c:
    print('a is greator')
elif b >= aa and b >= c:
    print('b is greator')
else:
    print('c is a greator')
    
#25. Wap to find the smallest of 3 numbers.
num1 = int(input('enter a num1'))
num2 = int(input('enter a num2'))
num3 = int(input('enter a num3'))
if num1 <= num2 and num1 <= num3:
    print('a is smallest')
elif num2 <= num1 and num2 <= num3:
    print('b is smallest')
else:
    print('c is a smallest')
    
#26.Wap to check the relation between two integer numbers.
one = int(input('enter a number1'))
two = int(input('enter a number2'))
if a > b:
    print(one, ">", two)
elif a < b:
    print(one, "<", two)
else:
    print(one, "==", two)
    
#27. Consider a character input if it is uppercase convert it into lowercase, if it is
#lowercase convert it into uppercase, if it is digit print the reminder when it is
#divided by 3 else if it is special character print it’s ASCII value.
char = input('enter a charcter')
if 'a' <= char <= 'z':
    print(char.upper())
elif 'A' <= char <= 'Z':
    print(char.lower())
elif: '0' <= char <= '9':
    print(int(char)%3)
else:
    print(ord(char)
          
#28.Wap to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the
#given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of
#both 3 and 5.
num = int(input('enter a num'))
if num %3 == 0:
          print('fizz')
elif num % 5==0:
    print('buzz')
elif num %3==0 and num % 5==0:
    print('fizzbuzz')
'''

ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print(chr(ord(ch) + 32))
elif 'a' <= ch <= 'z':
    print(chr(ord(ch) - 32))
elif '0' <= ch <= '9':
    print(int(ch) % 3)
else:
    print(ord(ch))
