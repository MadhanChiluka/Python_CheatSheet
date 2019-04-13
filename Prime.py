import math
num = int(input("Enter the number to check it is prime or not"))
for i in range(2, math.ceil(math.sqrt(num))+1):
    if num%i == 0 :
        print("It is not prime")
        break
else:
    print("It is Prime")