#profit exercise
cp=int(input('enter ur item cost price'))
sp=int(input('enter ur item selling price'))
profit=sp-cp
loss=cp-sp
if cp>sp:
    print('it will loss')
    print('the loss is',loss)
if sp>cp:
    print('it will profit')
    print('the profit is',profit)
#list example
a=[12,3,59,32]
b=['bhargavi','msc','cs']
print('the sorted list is',sorted(a))

a.append(32)
print(a)
mil=[a,b]
print(mil)

