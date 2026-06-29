# Boolean Functions

# any()  --> Returns True if at least one value is True


#Ex: 1
email = ""
phone = "0176-123456"
username = ""
# Allows registration
# if any field is filled
print(any([email, phone, username]))  # only phone True


#-------------------------------------------------------------------------------------------------

 
#all()  --> Returns True if all values are True

#Ex: 1
email = "abc@gmail.com"
phone = "0176-123456"
username = ""
# Allows registration
# only of all fields is filled
print(all([email, phone, username]))


#-------------------------------------------------------------------------------------------------


# isinstance (value, type)  --> chacks if a value bolongs to a certain data type

#Ex: 1
print(isinstance(123, int))         # True
print(isinstance("hello", str))     # True
print(isinstance(3.12,  float))     # True

age = 33.3

print(type(age))
print(isinstance(age, int))

