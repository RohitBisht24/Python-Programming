# Check whether two number are Co-Prime.
num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))
small = min(num1, num2)
is_co_prime = True
i = 2
while i < small:
    if num1%1==0 and num2%1==0:
        is_co_prime = True
    if num1%i==0 and num2%i==0:
        is_co_prime = False
        break
    i+=1

if is_co_prime:
    print("Co-Prime")
else:
    print("not Co-Prime")

        