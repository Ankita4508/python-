class A:
    def __init__(self, a,b,c):
        self.a=a
        self._b=b
        self.__c=c

    def __info(self):
        print('hello')

    #getter method to accesing the private method
    def get(self):
        print(self.__c)
        self.__info()
    #setter method to modifying the private method
    def set(self,n):
        self.__c=n

    #property getter method to modifying the private method
    @property
    def get2(self):
        print(self.__c)

    @get2.setter
    def get2(self,n):
        self.__c=n

ob1=A(1,2,3)

#accessing and modifyig the public property
print(ob1.a)
ob1.a=123
print(ob1.a)

#accessing and modifying the protect property
print(ob1._b)
ob1._b=345
print(ob1._b)



#accessing protect property and private method
#print(ob1.__c)
#ob1.__info()

#getter method to accesing the private method
ob1.get()
ob1.set(123)
ob1.get()

#setter method to modifying the private method
#ob1.set(123)

#property  method
#ob1.get2
#ob1.get2=543
#ob1.get2

#name mangling/syntax method
#access
#obname._classname__pn
#obname._classname__methodname

print(ob1._A__c)
ob1._A__c=555
print(ob1._A__c)
