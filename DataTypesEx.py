# DataTypes
# (int , float, bool, complex)

num = 2.5
print(type(num))

num1 = 2
print(type(num1))

num2 = 5+6j
print(type(num2))

k = int(num)
print(type(k))

com = complex(num1, k)
print(com)

print(num1 > 5)
bool = num1< 5
print(bool)
print(type(bool))
print(int(True))

lst = [10, 52, 50, 15]
print(type(lst))

tup = (10,20,30,40)
print(type(tup))

s = {10, 60,10, 52, 36,25,25}
print(type(s))

str = "Madhan"
print(type(str))

print(range(10))
print(set(range(10)))
print(list(range(2,10,2)))

dict = {'Madhan' : 'Iphone', 'Himaamshu' : 'Oneplus', 'Hithanshu' : 'MI'}
print(dict.keys())
print(dict.values())
print(dict['Madhan'])
print(dict.get('Hithanshu'))