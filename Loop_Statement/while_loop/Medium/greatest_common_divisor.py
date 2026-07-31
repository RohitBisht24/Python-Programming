# Find the GCD(greatest common divisor) of two numbers using while loop.

num1 = int(input("Enter the fist Number : "))
num2 = int(input("Enter the second Number : "))

# small = min(num1, num2)
i = 1
gcd = 1
while i <= min(num1, num2):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
    i += 1

print("Greatest Common Divisor : ", gcd)