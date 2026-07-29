# Print prime factors of a number.
num = int(input("Enter the Number : "))
fact = 0
i = 2
while i <= num:
    j = 2
    is_prime = True
    while j < i:
        if i % j == 0:
            is_prime = False
            break
        j+=1
    if is_prime:
        if num%i==0:
            fact = num//i
            print(i)
            num = fact
            i -= 1
    if num == 1:
        break
    i+=1
    

