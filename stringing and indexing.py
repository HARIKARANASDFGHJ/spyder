# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 19:34:47 2023

@author: harik
"""
string
var="language" 
print(len(var)) 
print(max(var)) 
print(min(var))
print(max(var)) 
print(sorted (var)) 
print(var.upper()) 
print(var.lower()) 
print(var.swapcase())
index() 
print(var.index('a'))
print(var.index('a',3))
print(var.index('a',6))
print(var.index ('a',3,6)) 
print(var.find('a'))
print(var.find('a',3))

print(var.index('a',-3))
print(var.index('l,-2'))
print(var.index('a',-2))
print(var.index('a',-6,-1))  


print(var.find('a',-3))
print(var.find('l,-2'))
print(var.find('a',-2))
print(var.find('a',-7,-1))   

var="language"

print(var.rfind('a',-3))
print(var.find('l,-2'))
print(var.find('a',-2))
print(var.find('a',-7,-1))  

print(var.rindex('a'))
print(var.rindex('a',3))   
print(var.index('a',-7))  
print(var.rindex('a',-7))              
var="python is a programming language"     
     #      title&hand 
print(var.title())           
(var.capitalize())     
              split() 
              var="language" 
              var.split('a') 
              var.split('a',1) 
              var.split('a',5)
              var.split('a',-1) 
              var.split('a',0) 
              var.split('z') 
              var.split('a',-5)    
              var.split ('n',2) 
              var.split ('a',2) 
              var.split ('a',3)
                 
              
                
              
                       replace  
                       var="replace"
                    print ( var.replace('p') ) 
                      var.replace('g','G')  
                      var.replace('g','G',1)  
                      var.replace('g','G',0) 
                      var.replace('g','g',-1) 
                      var.replace('p','p') 
                      var.replace('p','F',2) 
                      var.replace('p','A',2)
                       var.replace('r','F',-1)   
                       var.replace ('c','C')
                      var='Passionate Full-Stack Engineer '  
                      var.replace ('P','p') 
                      var.replace('a','A') 
                      var.replace ('t','T',2)
                       var.isupper()  
                       
                     other functions: 
                         var="language"
                         var.count('a') 
                         var.startswith('a') 
                         var.startswith('l') 
                         var .endswith('e')
                   important command:     
                       a=str(10) -int()
                       print(type(a)) -str()
                        b=int(2.0) -FLOAT
                        print(type(b)) -INT
                         
                        c=float(3)-INT
                        print(type(c))-FLOAT  
                        
                        
                      
                        
   
                        
   
    a=[22,44,54,78,2,3,10] 
    print(a[0]) 
    print(a[-2]) 
    print(len(a))
print(max(a)) 
print(min(a))
print(sorted(a))
print((a)) 
a.sort() 
print((a))      
                     


                             list: 
                                 
                          a=[22,44,54,78,2,3,10]       
                          a.append(99) 
                          print(a) 
                          a.insert(3,420)
                          print(a) 
                          print(a.pop()) 
                          print(a) 
                          del a[0] 
                          print(a)
                          print(a.remove(2)) 
                          print(a.remove(20))
                          print(a.count(54)) 
                          print(a.index(54))
                          print(a.index(20))
   
    
   b=["python","hari","harish"] 
   a.extend(b) 
   print(a) 
   
   shallow copy example: 
       a=[1,2,3] 
       b=a 
       a.append(6) 
       print(a) 
       print(b)
 deep copy example:
      a=[1,2,3]  
      b=a.copy() 
      a.append(6)
      print(a)
      print(b)  
        
      
        
      #others function 
      a=[22,44,54,78,2,3,10]
        a.reverse()
        print(a) 
        b=a.copy() 
        print(b)
        b.clear() 
        a=[1,2,3]*2 
        print(a)    
 
        
        
        
        functions that wont works 
        a=[22,44,54,78,2,4,10] 
        print(a.rindex(78)) 
        print(a.find (78)) 
        print(a.rfind(78))     
        
        
        
        
        list slicing: 
            
            a=[10,22,32,56,2,4,42] 
            print(a[:])  
            print(a[1:6])
            print (a[6:1]) 
            print (a[1:6:2]) 
            print(a[6:1:-2]) 
              
            
            print(a[-7:-2]) 
            print(a[-2:-7]) 
            print(a[-2:-7:-2]) 
            print(a[-7:-2:2])
    print(a[::-1]) 
    
    
    import random 
    a=[22,44,54,78,2,3,10] 
    print(random.choice(a)) 
    print(random.sample(a,2)) 
     (random.shuffle(a)) 
     print(a) 
     
     import random 
     print(random.random()) 
     print(random.randrange(0,500)) 
     print(random.uniform(1,5))
   
    
   lsit comprehension : 
       list=[x for x in range(1,10)] 
       print(list) 
       list_1=[x for x in range(2,10,2)] 
       print (list_1) 
       list_2=[x for x in range(1,10) if (x%2==1)]
       print (list_2)
 
    
 
