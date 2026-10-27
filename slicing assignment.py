Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
String 1: s = 'PYTHONPROGRAMMING'
1. Extract 'PYTHON'.
2. Extract 'PROGRAM'.
3. Extract the last 5 characters.
4. Reverse the entire string using slicing.
5. Print every alternate character
SyntaxError: invalid syntax

s = 'PYTHONPROGRAMMING'
s[:6:]
'PYTHON'
s[5::]
'NPROGRAMMING'
s[6::]
'PROGRAMMING'
s[:-5:]
'PYTHONPROGRA'
s[-5::]
'MMING'
s[::-1]
'GNIMMARGORPNOHTYP'
s[::2]
'PTOPORMIG'

String 2: s = 'DATASCIENCE'
1. Extract 'DATA'.
2. Extract 'SCI'.
3. Extract the last 4 characters.
4. Reverse only 'SCIENCE'.
5. Print characters at odd indices
SyntaxError: invalid syntax

a = 'DATASCIENCE'
a[:5:]
'DATAS'
a[:4:]
'DATA'
a[5:8:]
'CIE'
a[4:7:]
'SCI'
a[-4::]
'ENCE'
a[4::-1]
'SATAD'
a[-1:3:-1]
'ECNEICS'
a[:3:-1]
'ECNEICS'
a[1::2]
'AACEC'

String 3: s = 'MACHINELEARNING'
1. Extract 'MACHINE'.
2. Extract 'LEARN'.
3. Extract the first 10 characters.
4. Reverse the complete string.
5. Print every second character from the end.
SyntaxError: invalid syntax

b = = 'MACHINELEARNING'
SyntaxError: invalid syntax
b = 'MACHINELEARNING'
b[:7:]
'MACHINE'
b[7:12:]
'LEARN'
b[:10:]
'MACHINELEA'
b[:11:]
'MACHINELEAR'
b[::-1]
'GNINRAELENIHCAM'
b[::-2]
'GIREEICM'

String 4: s = 'ARTIFICIALINTELLIGENCE'
1. Extract 'ARTIFICIAL'.
2. Extract 'INTEL'.
3. Extract the last 8 characters.
4. Reverse only 'INTELLIGENCE'.
5. Print alternate characters
SyntaxError: invalid syntax

c = = 'ARTIFICIALINTELLIGENCE'
SyntaxError: invalid syntax
c = 'ARTIFICIALINTELLIGENCE'
s[:10:]
'PYTHONPROG'
c[:10:]
'ARTIFICIAL'
c[10:15:]
'INTEL'
c[:-9:-1]
'ECNEGILL'
c[:9:-1]
'ECNEGILLETNI'
c[::2]
'ATFCAITLIEC'

String 5: s = 'COMPUTERVISION'
1. Extract 'COMPUTER'.
2. Extract 'VISION'.
3. Extract the middle 5 characters.
4. Reverse the entire string.
5. Print characters from index 2 to index 10
SyntaxError: invalid syntax

d = 'COMPUTERVISION'
d[:8:]
'COMPUTER'
d[8::]
'VISION'
d[5:10:]
'TERVI'
d[::-1]
'NOISIVRETUPMOC'
d[2:11:]
'MPUTERVIS'

String 6: s = 'DEEPLEARNINGMODEL'
1. Extract 'DEEP'.
2. Extract 'LEARNING'.
3. Extract 'MODEL'.
4. Reverse only 'MODEL'.
5. Print every third character.
SyntaxError: invalid syntax

e = 'DEEPLEARNINGMODEL'
e
'DEEPLEARNINGMODEL'
e[:5:]
'DEEPL'
e[:4:]
'DEEP'
e[4:12:]
'LEARNING'
e[12::]
'MODEL'
e[:11:-1]
'LEDOM'
e[::3]
'DPAIME'

String 7: s = 'DATABASEMANAGEMENT'
1. Extract 'DATABASE'.
2. Extract 'MANAGE'.
3. Extract the last 7 characters.
4. Reverse the complete string.
5. Print alternate characters from the end.
SyntaxError: invalid syntax

f = 'DATABASEMANAGEMENT'
f[:8:]
'DATABASE'
f[8:14:]
'MANAGE'
f[-7::]
'AGEMENT'
f[::-1]
'TNEMEGANAMESABATAD'
f[::-2]
'TEEAAEAAA'

String 8: s = 'SOFTWAREDEVELOPMENT'
1. Extract 'SOFTWARE'.
2. Extract 'DEVELOP'.
3. Extract the last 5 characters.
4. Reverse only 'DEVELOPMENT'.
5. Print characters at even indices
SyntaxError: invalid syntax

g  = 'SOFTWAREDEVELOPMENT'
g[:8:]
'SOFTWARE'
g[8:15:]
'DEVELOP'
g[-5::]
'PMENT'
g[:7:-1]
'TNEMPOLEVED'
g[::2]
'SFWRDVLPET'

>>> String 9: s = 'CYBERSECURITY'
... 1. Extract 'CYBER'.
... 2. Extract 'SECUR'.
... 3. Extract the last 4 characters.
... 4. Reverse the entire string.
... 5. Print every alternate character from index 1
SyntaxError: invalid syntax
>>> 
>>> h = 'CYBERSECURITY'
>>> h[:6:]
'CYBERS'
>>> h[:5:]
'CYBER'
>>> h[5:10:]
'SECUR'
>>> h[-4::]
'RITY'
>>> h[::-1]
'YTIRUCESREBYC'
>>> h[1::-1]
'YC'
>>> h[1::-1]
'YC'
>>> h[0::-1]
'C'
>>> h[1::2]
'YESCRT'
>>> 'YESCRT'
'YESCRT'
>>> 
>>> String 10: s = 'INFORMATIONTECHNOLOGY'
... 1. Extract 'INFORMATION'.
... 2. Extract 'TECH'.
... 3. Extract 'NOLOGY'.
... 4. Reverse the complete string.
... 5. Print every third character
SyntaxError: invalid syntax
>>> 
>>> i = 'INFORMATIONTECHNOLOGY'
>>> i[:11:]
'INFORMATION'
>>> i[11:15:]
'TECH'
>>> i[15::]
'NOLOGY'
>>> i[::-1]
'YGOLONHCETNOITAMROFNI'
>>> i[::3]
'IOAOENO'
