file = open("File_handling/demo.txt", "r")

# print limited content
content = file.read(10)     #hello! i a
print(content)

# ----------------print only one line

# print first line3
line1 = file.readline()  
print(line1, end="")  

# print second line
line2 = file.readline()
print(line2,end="")  


line3 = file.readline()
print(line3,end="")  