# check Palindrome or not.
num = int(input("Enter the Number : "))
original_num = num
reverse = 0

while num > 0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num //= 10

if original_num == reverse:
    print("Palindrome Number.")
else:
    print("not a Palindrome.")
