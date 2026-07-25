a = 5
b = int(input("Enter 2nd Number : "))

try:  # try
    divide = a / b
except Exception as err:   #execpt
    print("Error : ",err)
else:           # else
    print("divide is : ",divide)
finally:        # finally
    print("main to hamesha print hounga.")  
print("\n")
print("\n")
print("hello world")
print("my name is rohit")
print("i love python programming")


# raise
age = int(input("enter the number : "))

if age > 18:
    print("adult")
else:
    raise TypeError("you age not eligible")

