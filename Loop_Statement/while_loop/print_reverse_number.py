num = int(input("Enter the Number : "))
i = 0
while num > 0:
    last = num % 10
    print(last,end="")
    num //= 10

