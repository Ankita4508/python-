class A:
    a = 10
    b = 20

ob1=A()
ob1.c=11
ob1.d=12

ob2=A()


print(A.a)
print(ob1.a)
print(ob2.a)

print(ob1.d)

print(A.a)
ob1.a=100
print(ob1.a)
print(A.a)
print(ob2.a)
print(ob1.c)
ob1.c=555
print(ob1.c)
