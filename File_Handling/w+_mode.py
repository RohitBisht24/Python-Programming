file = open("File_handling/demo.txt","w+")
file.write(input("Enter data : "))
print(file.read())
file.close()