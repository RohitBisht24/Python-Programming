#  cleaning(spaces) functions

# white space cleaning
    # lstrip 
    # rstrip 
    # strip 

#-----------------------------------------------------------------

# lstrip: (removes spaces from the left side of a string)

#Ex 1:
text = " Engineering".lstrip()
print(text)


#-----------------------------------------------------------------

# rstrip: (removes spaces from the right side of a string)

#Ex 1:
text = "Engineering".rstrip()
print(text)


#-----------------------------------------------------------------

# strip: (removes spaces from both ends)

#Ex 1:
text = "       Engineering ".strip()
print(text)


#Ex 2:
text = "##abc##".strip("#") # remove side hashes
print(text)


# -----------------------------------------------------

                        # how to detect extract spaces 
#chech the length before and after strip() to find unwanted spaces

#Ex 3:
text = "Engineering "
print(len(text))
print(len(text.strip()))  # detect extra spaces with len string function 

print("\n\n")

# detect spaces program
text = "Engineering"
print(len(text))
print(len(text.strip()))

number_of_spaces =  len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print("Number of Spaces: ", number_of_spaces)
print("Is my data clean? ", is_clean)




# -------------------------------------------------------------------------------
                                # Case Conversions

# lower() : Makes all letters lower case

#Ex 1: 
text = "PYTHON PROGRAMMING"
print(text.lower())


# upper() : Makes all letters upper case

#Ex 1: 
text = "python programming"
print(text.upper())


# clean data for matching
search = "Email ".lower().strip()
data = 'emAil'.lower().strip()

print(search == data)


#practice question
# Q1:  "968-maria, (D@t@ Engineer );; 27y " 
#       (name: maria | role: data engineer | age: 27)


