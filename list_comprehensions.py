# using loop
square = []

for i in range(6):
    square.append(i*i)
print(square)


#square using list comprehensions
square = [i*i for i in range(6)]
print(square)



# print square only odd numbers
square = [i*i for i in range(6) if i%2!=0]
print(square)



# if negative number print zero
num = [-2, -4, 3, 5, 2, -1]

result = [0 if val<0 else val for val in num ]
print(result)



# upper case using functions in list
word = ["hello", "python", "programming"]

upper_word =  [val.upper() for val in word]
print(upper_word)