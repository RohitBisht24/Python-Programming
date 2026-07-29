num = int(input("Enter the Number : "))

count = 0
while num > 0:
    num //= 10
    count +=1

print(count)