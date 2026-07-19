file = open(r"File_Handling/demo.txt","r+")
file.write(input("Enter Data : "))
content = file.read()
file.close()