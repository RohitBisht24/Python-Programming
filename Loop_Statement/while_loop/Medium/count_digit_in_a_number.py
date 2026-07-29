num = int(input("Enter the Number : "))

num = abs(num)  # Handles negative numbers

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10

print("Total Number of Digit : ", count)