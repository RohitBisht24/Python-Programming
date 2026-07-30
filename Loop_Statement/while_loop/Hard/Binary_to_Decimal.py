# Convert Binary to Decimal using while loop.
num = int(input("Enter the Number : "))
sum = 0
pow = 0
while num > 0:
    LD = num % 10 
    sum += LD*(2**pow)
    num //= 10
    pow+=1

print(sum)