#Decorators
#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, 
#without permanently modifying it.

def div(a,b): 
    if a<b: 
        a,b = b,a 
        print (a/b)
        
div(2,4)
      
#Using Decorators       
     

def div(a,b): 
    print (a/b)
    
def sub(a,b):
    print((a-b))
    
def smart_div(func):
    
    def inner(a,b): 
        if a<b: 
            a, b = b, a 
        return func(a,b)
    return inner
    
divide= smart_div(div)
subtract = smart_div(sub)
divide(5,10)
subtract(5,10)

#Iterators

#Iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. 
#The iterator object is initialized using the iter() method. It uses the next() method for iteration.

#__iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
#__next__(): The next method returns the next value for the iterable. 
#When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator 
#object, which further uses the next() method to iterate over. 
#This method raises a StopIteration to signal the end of the iteration.

nums = [6,7,8,9]

#1st way-------------------------------
print(nums[2])

#2nd way-------------------------------
for i in nums:
    
    print(i)
    
#3rd way Iterator way------------------

it = iter(nums)

print(it) #------> prints the iterator object

print(it.__next__())   

#or

print(next(it))

# so it stores the before value so it gives the next value

for i in nums:
    
    print(i)
    
#Example of Iterator

class TopTen:
    
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num += 1
        
            return val
        else:
            raise StopIteration
            
            # to stop a for loop, raising an exception is the only way 
    
values = TopTen()

#uncomment below and run to see te beauty of iterator
print(next(values))
    
for i in values:
    print(i)
    
#Generator

#Generator-Function: A generator-function is defined like a normal function, 
#but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
#If the body of a def contains yield, the function automatically becomes a generator function.

#Generator-Object : Generator functions return a generator object. 
#Generator objects are used either by calling the next method on the generator object
# or using the generator object in a “for in” loop (as shown in the above program).

#Diff between return and yield
def topten():
    
    #return 5
    yield 5
    
values = topten()

print(values)

#to return a value from iterator we need to use the next function

def topten():
    
    yield 1
    
values = topten()

print(values.__next__())    

# to get multiple values

def topten():
    
    yield 1
    yield 2
    yield 3
    yield 4
    
values = topten()

print(values.__next__())
print(values.__next__())

for i in values:
    print(i)
    
#Example

def topten():
    
    n=1
    
    while n<=10:
        sq = n*n
        yield sq
        #its almost same to return, just return will terminate but this yield will not
        n += 1
   
values = topten()

print(values.__next__())
for i in values:
    print(i)

#Application: If we are processing 1000 records, it will all get stored. We dont need that, so we will take 
#each record and work on it individually 




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    