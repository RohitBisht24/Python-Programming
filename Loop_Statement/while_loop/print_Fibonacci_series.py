# Print Fibonacci series up to N terms.
num = int(input("Enter the Number : "))

i = 0
a = 0
b = 1

while(i < num):
    print(i,end=",")
    
    c = a + b
    a = b
    b = c
    i+=1
    

   