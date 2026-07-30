# convert Decimal to Binary using while loop.
num = int(input("Enter the Number : "))
binary = ""
while num >= 1:
    remainder = num % 2
    binary = str(remainder) + binary
    num //= 2

print(binary)




