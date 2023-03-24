# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 06:47:22 2023

@author: harik
"""

control statement 



for i in range(1,5) :
    if(i==3): 
        break 
    print(i)
      

for i in range(1,5) :
    if(i==3): 
        continue
    print(i)
      
for i in range(1,5) :
    if(i==3): 
        pass
    print(i)
      
               lambda function 
             
                
             
a=lambda :5+4 
print(a())
a=lambda x:x*2 
print(a(2))
a=lambda x,y,z:x+y-z 
print(a(1,2,3))
import math 
a=lambda x:math.factorial(x) 
print(a(3))
a=lambda x:sum (x) 
b=[5,2,3]
print(a(b))
a=lambda x,y,z extend (y)
b=[1,2,3]
c=[1,2]
print(b)
a=lambda x:x. update({7:3})
b={1:1,2:2,3:3}
a(b)
print(a(b))
print(b)
 

                       filter 
 
    
def  even (n):
    if(n%2==0): 
        return True 
    else: 
        return False 
    
    
a=[1,2,3,4,5,6,7,8] 
print(list(filter(even,a))) 




a=[1,2,3,4,5,6,7] 
print(list(filter(lambda n:n%2==0,a)))
 


                             map() 
                             

def  even (n): 
    if(n%2==0): 
        return True 
    else: 
        return False 
  
a=[1,2,3,4,5,6,7]   
print(list(map(even,a)))
a=[1,2,3,4,5,6,7] 
print(list(map(lambda n:n%2==0,a)))
  

                           my math() 
import math

print("I am in test.py")
math.calculate_area(5,10)
