def fact(n):
    if n==1:
        return 1
    else:
        for i in range(1,n+1):
            return fact(n)*i
def main():
    num=int(input('enter a num'))
    fact(num)
main()


