#keysinpython
'''import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))'''

#unary
'''a=~7
print(a)'''
'''a=~(-7)
print(a)'''
#leapyear
'''year=int(input())
if year%4==0:r
 if year%100==0:
  if year%400==0:
   print("leap year")
  else:
   print("its not a leap year")
 else:
  print("its  a leap year")
else:
 print("its not a leap year")'''
#list
'''li=[]
print(type(li))
l2=[4,3.6,8+2j,True,False,'aits','r']
print(l2)
for i in l2:
    print(i)
for i in l2:
    print(i,end=' ')
print(l2[3])#subscript
print(l2[2:len(l2)+1])#slice
print(l2[::])
print(l2[::2])
print(l2[::-1])'''
#listinruntime
'''lis=list()
for i in range(5):
    lis.append(int(input()))
print(lis)
n='kusuma','kumari'
print(list(n))
n1=range(1,4)
print(list(n1))'''
#list
'''pl=['korea','dubai','bangkock','goa']
print(len(pl))#shows the length of the list
print(max(pl))#gives the maximum value based on the homogenious alphabetic order
print(min(pl))#gives the minimum value """"
#print(max(len(int(pl))))
#print(sum(pl))#sum the list
print(sorted(pl,reverse=True))#gives the sorted order of the list,sort temporary,reverse
print(list(pl))#to create a new list
print(any(pl))#return true if valuehave atleast one true value
print(all(pl))#return true if all the values have the treu value'''
# false values are 0,0.0,0+0j,"",None,False,[],(),{},set()
#operators on list
#+=it is used to add two list into a single list
#* = it is used to list multiplication
'''a1=[1,2,3]
a2=[567,567,567]
print(a1+a2)
print(a2*5)
a3=[]
print(a3*5)'''
#relational operator
#methods of list
#append
#extend
#insert
#index
#count
#remove
#pop
#clear
#sort
#reverse
'''pl2=['korea','dubai','bangkock','goa']
pl3=['viz','bhapatla']
pl2.append('kerala')
print(pl2)
pl2.extend(pl3)
print(pl2)
pl3.insert(2,'pune')
print(pl3)
print(pl2.index('goa'))
print(pl2.count('goa'))
pl2.remove('bangkock')
print(pl2)
pl2.pop()
print(pl2)
pl2.pop(4)
print(pl2)
#pl2.pop(12)
#print(pl2)
pl2.clear()
print(pl2)
pl3.reverse()
print(pl3)
pl2.sort(reverse=True)
print(pl2)
del pl2
print(pl2)'''
'''def cat(c,n,u,arr):
    if n==0:
        return 0
    cf=0
    rf=c*u
    for i in arr:
        cf+=arr[i]
        if (cf>rf):
            return i+1
    if(cf<rf):
        return -1
n=int(input())
c=int(input())
u=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(cat(c,n,u,arr))'''
#missing value
'''def missing(n):
    b=[]
    for i in range(10):
        if i not in n:
            b.append(i)
    print(b)
                
n=list(input())
missing(n)'''
'''def missing(num):
    li=[False]*10
    while num:
        li[num%10]=True
        num=num//10
    return li
num=int(input())
res=missing(num)
for i in range(10):
    if not res[i]:
        print(i,end=' ')'''
#print([a*a for a in range(1,6)])
#print(x*x for x in range  (1,16) if x%2==1 if x%3
#n=int(input())
#print(['fizz' if i%n==0 else 'buzz' for i in range(1,16)])


#copy method
'''a1=[1,2,3]
a2=a1.copy()
a2.append(21)
print(a2)
print(a1)'''
l1=[21,16,14]
print(id(l1))
l1.append(15)
print(l1)
l1.remove(14)
print(id(l1))
