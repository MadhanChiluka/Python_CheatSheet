i = 1
while i<=6:
    print("Madhan", end = " ")
    i+=1
print()
lst = [10, "Madhan",  "25"]
for i in lst:
    print(i)
for j in range(1,10,2):
    print(j)

availableCandies = 10
candiesNeeded = int(input("How many candies you need?"))
i=1
while i <= candiesNeeded:
    if(i > availableCandies):
        print("No Stock")
        break

    print("Candy", i)
    i+=1


for i in range(1, 101):
    if (i%3 == 0 and i%5 == 0 or i%4 == 0):
        continue
    print(i, end = " ")
