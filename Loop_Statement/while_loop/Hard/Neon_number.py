# check whether a number is Neon number.

num = int(input("Enter the Number : "))
square = num**2
sum = 0
while square > 0:
    LD = square % 10
    sum += LD
    square //= 10

if num == sum:
    print(f"{num} is a Neon Number.")
else:
    print(f"{num} is not a Neon Number.")
