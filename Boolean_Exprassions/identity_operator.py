# # Indentity Operator
# # checks if two variable refer to the same object in memory

#Ex: 1
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y)   # checking the value are same or not
print(x is y)   # checking object id(address) are same or not


#Ex: 2
x = ['a', 'b', 'c']
y = x
print(x is y)



# # get address as a decimal integer
# print(id(x))
# print(id(y))

# # convert address to standard hexadecimal format
# print(hex(x))
# print(hex(y))
