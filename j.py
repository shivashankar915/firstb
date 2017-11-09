"""
def list1(a,b):
    count=0
    for i in range(len(a)):
        if a[i]==b[i]:
            print("print is equal")
        else:
            print("not eual")
lis2=[1,2]
lis3=[12,34]
d=list(map(list1(),a,b))
print(d)
"""
"""
a=[5,6,7,8,9,10]
b=[5,8,9,10]
def print1(x):
    if(x>9):
        return x
    

f=list(filter(print1,a))
print(f)
"""

list1=[1,2,3,4]
list2=[1,2,4,5]
list3=[(x[i],y[i]) for x in list1 for y in list2 if x==y]
print(list3)

list1=[1,2,3,4]
list2=[1,2,4,5]
lenght=len(list1)
lenght1=len(list2)
for x in range(lenght):
    for y in (lenght1):
        if (x[]==y[]):
            print((x,y))
        
   
    
    



    



    
