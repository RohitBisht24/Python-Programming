# check Prime Number or not
num = int(input("Enter the Number : "))

i = 2
is_prime = True

if (num == 1):
    print("Non Prime Number.")
else:
    while (i < num):
        if num % i == 0:
            is_prime = False
        i += 1

    if is_prime == True:
        print("Prime Number.")
    else:
        print("Non Prime Number.")