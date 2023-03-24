# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:36:13 2023

@author: harik
"""
  #  acess specifier 
  #encapsulation
  
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
        
#encapsulation

class Add:
    def __init__(self,a,b,c):
        self._a=a
        self.__b=b
        self.c=c
    def  add(self):
        f=self.__b+self.c
        return f
    
if __name__=="__main__":
    value=Add(10,21,14)
    print(value.add())
    value.__b = 20
    

    
    
    
    
class Add:
    def __int__(self,a,b,c): 
        self._a=a #protect 
        self.__b=b #private  
        self.c=c #public 
    def add(self): 
        #d=self._a+self.c 
        f=self.__b+self.c 
        return f 
    
    if __name__=="__main__": 
        value =add(10,21,14) 
        print(value.add()) 
        value.__a=20
        print(value.add()) 
        value.__b=20 
        print(value.add()) 
        
        
                             encapsulation
class student(): 
    def __int__(self,Name,id): 
        self.Name=Name 
        self.id=id 
        
st=student("python",11) 
print(st.Name) 
st.Name="languange" 
print(st.Name)
 

                             INHERITANCE 
                             
                             
   1.SINGLE IN HERITANCE   #no constructor in parent and child clases
class parent(): 
    def sent_money(self): 
        self.money=5000 
class child(parent): 
    def get_money(self):
        self.sent_money() 
        print(self.money)
C_obj=child() 
C_obj.get_money()                            


2.mulitilevel inheritance 


class parent(): 
    def __init__(self): 
        pass 
    def eat(self): 
        print("parent eat function called") 
        
class child(parent): 
    def __init__(self): 
        pass 
     
class Grand_child(child):
    def __init__(self): 
        self .eat() 
        
        
C_obj=Grand_child()