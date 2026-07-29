# Find the GCD of two numbers using while loop.

num1 = int(input("Enter the fist Number : "))
num2 = int(input("Enter the second Number : "))

i = 2
while True:
    if num1 % i == 0 and num2 % i == 0:
        print(f"{num1} and {num2} is greater common divisor num : {i}")
        break
    i += 1