# Data Transformation 

                    # replace(old, new)

# swaps part of the text with something new

#Ex 1:
price = "1234,56"
change = price.replace(",", ".")
print(change)   #1234.56

#Ex 2:
date = "19/06/2026"
result = date.replace("/" , "-")
print(result)   #19-06-2026

# note: replace() is not just for changing values you can alsop remove unwnated parts by replacing them with as empty string("")

#Ex 3:
price1 = "$1,299.99"
print(price1.replace("$", "").replace("," , ""))


# practice ("+49 (176) 123-4567" - 00491761234567)
practice = "+49 (176) 123-4567"
print(practice.replace(" ", "").replace("+", "00").replace("-", "").replace("(", "").replace(")", ""))


#-----------------------------------------------------------------------------


                        #'string' + 'string'

# join (concatinates) two string into one.

#Ex 1:
first_name = "Rohit"
last_name = "Bisht"
last_name = first_name +" "+ last_name

print(last_name)

#Ex 2:
folder = "C:/Users/Rohit/"
file = "reprot.csv"
full_file_path = folder + file
print(full_file_path)


#-----------------------------------------------------------------------------


                        #f-string

# Modern, super-easy way to format and build strings "f" stands for "formatted" 
# lets you easily put variables and expressions directly inside string value

#Ex 1:
name = "Rohit"
age = 22
is_student = False
print("My name is "+name+", I am "+ str(age) + " years old, and student status is " + str(is_student) +".")

        # normal format to f-string format 

print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")

#Ex 2:
print(f"2 + 3 = {2+3}")

#Ex 3:
#print(f"({this is me})")   through error because this not variable and expression
  

#-----------------------------------------------------------------------------
 

                        # Split()

# break a sting into smaller parts

#Ex 1:
stamp = "19-06-2026"
print(stamp.split("-"))

#Ex 2:
input = "Adan-24-USA"

spliting = input.split("-")
print(spliting)

name = spliting[0]
number = spliting[1]
country = spliting[2]

print(f"name is : {name}")
print(f"number is : {number}")
print(f"country is : {country}")

#Ex 3:
csv_file = "123,max,USA,1970-10-05,M"
result = csv_file.split(",")
print(result)


#-----------------------------------------------------------------

                        # 'string' + number

# Repeats the string multiple times

#Ex 1:
print("ha" * 3)

#Ex 2:
print("#" * 30)


#-----------------------------------------------------------------

                    # Data Extraction(Indexing & slicing)
                    
# indexing : extracts one character by position.

#Ex 1: 
text = "Python"

#Extract the first character
print(text[-6])
print(text[0])

#Extrat the last character
print(text[-1])
print(text[5])

#Extrat h
print(text[3])


#-----------------------------------------------------------------


# Slicing : Extracts a part of the string

date = "19-06-2026"

#Extract the date
print(date[:2])
print(date[0:2])

#Extract the month
print(date[3:5])

#Extract the year
print(date[6:])