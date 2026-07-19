file = open("File_handling/demo.txt","a+")
file.write(f"{input("Enter data : ")}\n")
print(file.read())
file.close()