# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 19:20:27 2023

@author: harik
"""

print (isinstance(9,int))
print(isinstance(9,str))
a=str(10) 
print(type(a))
print(isinstance(a,int))
print(isinstance(1+3j,int))
a=int(9) 
print(isinstance(a,int))
a=list("hari") 
print (type(a)) 
print (isinstance(a,list))
a=int(9) 
print (type(a)) 
print(isinstance(a,int))
a=(20.5)
print (type(a)) 
print(isinstance(a,float))







b=(10,12,13) 
print(type(b))
print (isinstance(b,tuple))
a= ("apple", "banana", "cherry")
print(type(a))
print(isinstance(a,tuple)) 
  



a = {"apple", "banana", "cherry"} 
print(type(a)) 
print (isinstance(a,set)) 


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(type(thisdict)) 
print (isinstance(thisdict,dict)) 


