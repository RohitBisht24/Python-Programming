# strong numbers

num = int(input("Enter a number. : "))

i = 1
factorial = 1
original = num

while num > 0:
    last_digit = num % 10

    while i <= last_digit :
        factorial = factorial*i
        i += 1

    total =  total +   factorial
    num = num // 10

if total ==  original:
    print("It is a strong number.")
