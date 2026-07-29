num = int(input("Enter the number : "))
big = 0

while num > 0:
    last = num % 10 

    if big < last:
        big = last

    num = num // 10

print(big)
