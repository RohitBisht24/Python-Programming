# class & Instance Attributes

class student:
    college_Name = 'IIT BHU'
    name = "anonymous"   # class attribute

    def __init__(self, name, age):
        # print(self)
        self.name = name   # obj attribute  > class attribute
        self.age =  age
        print("Adding new student in Database..")

s1 = student("karan", 21)
print(s1.name, s1.age)

s2 = student("arjun", 33)
print(s2.name, s2.age)


print(s1.college_Name)
print(s1.name)