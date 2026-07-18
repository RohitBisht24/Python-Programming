# oppent mode (a)  --> open for writing, appending to the end of th file if if exists ;-

file = open("File_Handling/demo.txt", "a")  # read file
writting_content = file.write(f"\n{input("Enter data : ")}")
file.close()


# read file
file1 = open("File_Handling/demo.txt", "r")  # read file
read_content = file1.read()
print(read_content)
file1.close()
