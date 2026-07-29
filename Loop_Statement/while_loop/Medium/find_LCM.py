num1 = int(input("Enter the first Number : "))
num2 = int(input("Enter the second Number : "))

lcm = max(num1, num2)

try:
    while lcm % num1 != 0 or lcm % num2 != 0:
        lcm+=1
except Exception as err:
    print("Error:",err)
else:
    print("LCM is : ",lcm)