string = "Hello"

# in --> memebership operator

# Ex:1
# print hello sequentialy
for var in string:
    print(var)


# Ex:2
# check in membership function
if 'o' in string:
    print("o exists in string")
else:
    print("Not exists in string")


# Ex:3
# print number 1 to 5
for i in range(5):
    print(i+1)


#Ex:4
word = "artificial intelligence"
# count the number of i's =  5

count = 0
for var in word:
    if var == "i" :
        count +=1

print(count)


