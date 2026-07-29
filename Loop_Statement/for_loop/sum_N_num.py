# Sum of first N natural Number.

num = int(input("Enter the Number : "))
sum = 0
for i in range(1,num+1):
    sum += i

print("sum is : ",sum)



# we can write without using loop
num = int(input("Enter the number : "))

sum = num*(num+1)//2

print("Sum is : ",sum)

