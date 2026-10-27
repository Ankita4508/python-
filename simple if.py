#check whether the number is even.
'''
n=int(input('Enter the number:'))
if n%2==0:
    print('Even')


s=input('Enter the string:')
if  len(s)==5:
    print('Given sring is of length 5 ')

'''


#1. Wap to print the square of a number only if it is even.
n = int(input('Enter the num'))
if n%2==0:
    print(n*n)
#2. Wap to check whether the character is vowel or not.
    
c = input('Enter the character')
if c in 'aeiouAEIOU':
    print('vowel')
        
#3. Wap to print Ascii value of a character only if it is upper case.
#4. Wap to print the cube of a number only if it is divisible by 9 or 6.
d = int(input('Enter the num'))
if d%9==0 or d%6==0:
    print(d*d*d)
#5. Wap to check whether the given integer is 3 Digit number.
a = int(input('Enter the integer : '))
if 100 <= a <= 999:
    print('3 digit num')
#. Wap to check whether the last digit of a given number is 5.
b = int(input('Enter the num'))
num = b%10
if num==5:
    print('last num is 5')
#7. Wap to check whether the given data is float.
e = eval(input('Enter the data'))
if type(e)== float:
    print('float')
#8. Wap to check whether the data is single value data.
data = eval(input('Enter the data'))
if data == float or int or bool or complex:
    print('single value data')
#9. Wap to check whether the given character is digit or not.
digit = eval(input('Enter the character'))
if digit == int or float or complex:
    print('its a digit')
#10.Wap to check whether the given integer is multiple of 3.
multi = int(input('Enter the num'))
if multi % 3 == 0:
    print('multiple of 3')
                
