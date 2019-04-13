from array import *
vals=array('i',[12,64,76,19,23,59])

print(vals)
newarr=array(vals.typecode,(a*a for a in vals))
for e in newarr:
    print(e)
