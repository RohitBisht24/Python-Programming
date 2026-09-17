num = int(input("Enter the Number : "))

for i in range(0, num+1):
    for j in range(1, num-i+1):
        print("*", end=" ")
    print()
