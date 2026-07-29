num = int(input("Enter the Number : "))

# original = num
# total = 0

while num > 0:
    last_digit = num % 10

    # find factorial of the digit
    fact = 1
    i = 1
    while i <= last_digit:
        fact *= i
        i += 1

# total+=fact
print(fact)
