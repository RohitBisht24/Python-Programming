num = int(input("Enter the Number : "))
digit = 0

while digit <= 9:
    temp = num
    count = 0

    while temp > 0:
        last_digit = temp % 10

        if last_digit == digit:
            count += 1 

        temp //= 10

    if count > 0:
        print(digit,";", count)

    digit += 1