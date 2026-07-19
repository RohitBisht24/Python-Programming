# check Armstrong or not.
num = int(input("Enter the number : "))
original = num
armstrong = 0
while (num > 0):
    last = num % 10
    armstrong = armstrong + (last ** 3) 
    num //= 10

if original == armstrong:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
