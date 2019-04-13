from array import *
val=array('i',[])
n=int(input('enter a len of array'))
for i in range(n):
   x= int(input('enter the next val'))
   val.append(x)
   print(val)
k=0
key=int(input('enter the valu to be searched'))
for e in val:
    if e==key:
        print(k)
        break
        k+=1