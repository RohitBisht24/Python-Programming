# check whether a number is Heppy Number or not.
num = int(input("Enter the Number : "))
sum = 0

while num != 1 and num != 4:
    sum = 0
    while num > 0:
        last1 = num % 10
        sum = sum + (last1**2)
        num //= 10
    if sum == 1:
        break
    num = sum

if sum == 1:
    print("Happy Number.")
else:
    print("Non-Happy Number.")
    
    