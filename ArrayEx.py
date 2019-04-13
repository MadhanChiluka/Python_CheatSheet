import array as arr
val = arr.array('i', [10,20,62,-52])
print(val)
for i in range(len(val)):
    print(val[i])
for e in val:
    print(e)

oldArr = arr.array('i', [10, 82, 15, 27, 25])
newArr = arr.array(oldArr.typecode, (a*a for a in oldArr))
for m in newArr:
    print(m)