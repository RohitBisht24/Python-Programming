# List Methods (Build-in Functions)



# Slicing in list

numbers = [10, 20, 30, 40, 50]


print(numbers[1:4])     # [20,30,40]

print(numbers[:3])      # [10,20,30]

print(numbers[2:])      # [30,40,50]

print(numbers[::-1])    # [50,40,30,20,10]



# append()  -->  Adds one elements at the end.

numbers.append(10)
print(numbers)


# extend ()  -->  Adds multiple elements

numbers.extend(["rohit", "Sheriyans", True])
print(numbers)



# inest()  -->  Insert at a specific position.

numbers.insert(1, 000)
print(numbers)



# remove()  -->  Removes the first Matching values.

numbers.remove(12)
print(numbers)



# Pop()  -->  Removes an elements by index.

numbers.pop(0)
print(numbers)



# clear()  -->  Removes all elements

numbers.clear()
print(numbers)



# index()  -->  Returns the index of a value.

print(numbers.index(12))  # as works line find in string



# count()  -->  Counts Occurrences

print(numbers.count(12))



# sort()  -->  sorting list in (Ascending order)

marks.sort()
print(numbers)



# sorted()  --> sorting list with print same line (Ascending order)
print(sorted(numbers))



# sort(reverse = True)  -->  soting list in reverse (descending order)

numbers.sort(reverse=True)
print(numbers)



# reverse()  -->  reverse list

numbers.reverse()
print(numbers)



# copy

marks = numbers.copy()
print(number)



# len()  -->  return the length of the list
print(len(numbers))



# del  -->  for deleting elements in list

del numbers[-4:]

print(marks)



# sum()  -->  sum element in list

print(sum(marks))



# min  -->  returns minimum element

print(min(marks))



# max()  -->  returns maximum element

print(max(marks))


# in  

print(20 in numbers)    # True

print(100 in numbers)   # False

# not in
def jls_extract_def():
    # False
    return 


print(50 not in numbers)    # False = jls_extract_def()


















