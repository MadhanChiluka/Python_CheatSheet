print("Hello World")

print('madhan\'s "laptop"')

print(10 * 'madhan')

print('c:\docs\naveen')
print(r'c:\docs\naveen')
myname = "Madhan"
print(len(myname))
print(myname[0:3])
nums =  [12, 52, 42, 25, 25, "Madhan"]
print(nums)

names = ["Himaamshu", "Hithanshu", "Madhan", "Bhargavi"]

twoArrays = [nums, names]

nums.append(45)
print(nums)

nums.remove(45)

print(nums)

nums.insert(2, 45)

print(nums)
nums.pop(2)
print(nums)

print(nums.pop())
del nums[2:]

print(nums)
print(twoArrays)
for i in nums :
    print(nums[i])