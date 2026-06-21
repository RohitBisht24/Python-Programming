# Searching

# Startswith()

# Ex: 1
phone = "+91-730-287-2568"
print(phone.startswith("+91"))


# endswith()

# Ex: 1
email = "rohit@gmail.com"
# email = "rohit@outlook.com"    False
print(email.endswith("gmail.com"))

# Ex: 2
file = "data_backup.csv"
print(file.endswith(".csv"))


# in()

# Ex: 1
email = "rohit@outlook.com"
print("@" in email)

# Ex: 2
urls = "https://api.company.com/v1/data"
print("/api" in urls)




# Find


#Ex:  1

phone1 = "+91-123-456-7894"
phone2 = "46-495-89544"
phone3 = "0046-2495-89544" 

print(phone1[4:])
print(phone2[3:])

print(phone1.find("-"))