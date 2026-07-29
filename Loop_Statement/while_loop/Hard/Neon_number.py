# check whether a number is Neon number.
num = int(input("Enter the Number : "))
square = num**2
sum = 0
while square > 0:
    # square = num**2
    LD = square % 10
    sum += LD
    square //= 10

if num == sum:
    print("same ")
else:
    print("not a same")
