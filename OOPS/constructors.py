class student:
    # constructor
    def __init__(self, fullname, marks):
        self.name = fullname
        self.mark =  marks
        print("creating new student")

obj = student("Rohit", 89)
print(obj.name, obj.mark)


  ##=================================================================================


# default constructors
class student:
    def __init__(self):
        print("Adding new student in Database..")

# Parameterized constructors
class student:
    def __init__(self, name, age):
        self.name = name
        self.age =  age
        print("Adding new student in Database..")