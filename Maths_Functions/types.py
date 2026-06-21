# Categories : Types

# type()

a = 23
b = 3.14
c = 2 + 3j
print(type(a))
print(type(b))
print(type(c))



# int()  --> converts compatible value into int value

# stirng to integer
x = "24"
result = type(int(x))
print(f'x = "24" converts into integer : {int(x)} {result}')

# conversoin float to integer
x = 3.14
result = type(int(x))
print(f"x = {x} converts into integer : {int(x)} {result}")



# float() -->  converts compatible value into float value

# int to float
x = 12
result = type(float(x))
print(f"x = {x} converts into float : {result}")

# string to float
x = "3.14"
result = type(float(x))
print(f'x = "3.14" converts into float : {result}')



# complex (real, imaginary)  -->  create a complex number using real and imaginary parts

 #Ex: 1
x = 3   # real
y = 4   # imaginary

print(f"complex: {complex(x, y)}")




