word = input("Enter the word : ")
new_word = word.lower()

count = 0
for var in new_word:
    if var in ('a', 'e', 'i','o','u'):
        print(var,end=", ")
        count += 1
    
print("\n",count)