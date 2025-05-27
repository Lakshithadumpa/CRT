#dictonery are used to store key and value pairs which are ordered ,mutable,and allows duplicate elements in values
#we can store elements inside {} brases in the form of key and values 
#inorder to add a new key we can use the below syntax
#sytax: obj.['key']='value'
#if the key exist the value will be replaced or else a key will be added to the dictonary

'''def cricket(n):
    d={}
    for i in range(n):
        a=list(input())
        b=list(input())
        d[a]=b
    print(d)
n=int(input())
print(max(d.values()))   
cricket(n)'''
#dicrionary comprehensions
#syntax: {key:value for (k,v) in iterable}
#print({k:k*k for k in range(10,16) if k%2==0})
#names=['vinodh','viha','vihansh','lakshitha']
#print({name:len(name) for name in names})
#print({name:'dteam' if len(name)%2==0 else 'mteam' for name in names if len(name)>3})
'''name=input()
d={i:name.count(i) for i in name}
print(d)'''
#import collections
#counter
#defaultdict
#deque
#namedtuple
from collections import Counter#syntax variable=counter(sequence)
from collections import defaultdict#syntax variable=counter(sequence)

'''string="My name lakshitha"
var=Counter(string)
print(var)'''
import random
'''s= [random.randrange(1,8)for i in range(10)]
var=Counter(s)
print(var)'''
#defaultdict is sub class of inbuilt class dict syntax: var=defaultdict(default_factory)
'''d=defaultdict(int)
d['a']=1
d['b']=2
print(d['a'])
print(d['b'])
print(d['c'])#wont raise keu error return 0.'''
'''d=defaultdict(list)
d['cricket'].append('kohil')
d['batminton'].append('sindu')
print(d['cricket'])
print(d['football'])'''
#deque
#itmeans
#generally queue follows FIFO structure but in deque it supports FIFO
#it will accept list as argument SYNTAX: var=deque(list)
'''from collections import deque
d=deque([3,4,5])
d.append(6)
print(d)

d.appendleft(1)
print(d)

d.pop()
print(d)

d.popleft()
print(d)
d.extend([1,2,3])
print(d)

d.extendleft([-2,-2,0])
print(d)
d.remove(5)
print(d)

d.rotate(3)#+right -left
print(d)'''

#namedtuple
# it is a mini class we can acces elements using name
# SYNTAX : var=(type_name,field_names)
student=namedtuple('student',['name','branch','marks'])
s1=('student','kiran','cse','508')
print(s1.name)
print(s1.marks)
print(s1.branch)
#dictionary nesting and data transformations


        
