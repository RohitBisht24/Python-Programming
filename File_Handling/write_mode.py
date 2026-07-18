file = open("File_Handling/demo.txt","w")  # open file

# write file
writting_data = file.write(input("Enter data : "))
print("Length of data : ",writting_data )

file.close()

# read file
file1 = open("File_Handling/demo.txt","r")
content = file1.read()
print(content)

file1.close()

