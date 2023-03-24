#Encapsulation
#acces modifier - private, protect, public
class A:
    def __init__(self,a,b):
        self.__a=a
        self.b=b
    def add(self):
        c=self.__a+self.b 
        return c

        
if __name__=="__main__":
   obj=A(30,30)
   obj.__a=50
   print(obj.add())
   
class Add:
    def __init__(self,a,b,c):
        self._a=a #protect
        self.__b=b #private
        self.c=c #public
    def add(self):
        #d=self._a+self.c
        f=self.__b+self.c
        return f

if __name__=="__main__":
    value=Add(10,21,14)
    print(value.add())
    #value._a=20
    #print(value.add())
    value.__b=20
    print(value.add())
    
    