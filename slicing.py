Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'Today is Tuesday'
>>> s
'Today is Tuesday'
>>> s[6:8:1]
'is'
>>> s[0:5:1]
'Today'
>>> #dyi us
>>> s[2:13:2]
'dyi us'
>>> #yad
>>> [5:4:-1]
SyntaxError: invalid syntax
>>> [5:1:-1]
SyntaxError: invalid syntax
>>> s[5:4:-1]
' '
>>> s[5:1:-1]
' yad'
>>> s[4:1:-1]
'yad'
>>> s[0:5:]
'Today'
>>> s[::2]
'Tdyi usa'
>>> s[1::2]
'oa sTedy'
>>> s[::-1]
'yadseuT si yadoT'
>>> s[1::2]
'oa sTedy'
