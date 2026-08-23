# type of method

# instance  methods  (self)

class student:
    def show(self):
        print("hellow world")

s1 = student()
s1.show()


# class method     @classmethod

class student:
    college = "IIT BHU"

@classmethod
def show_college(cls):
    print(cls.college)

student.show_college()


# static method   @staticmethod

class student:
    @staticmethod
    def add(a, b):
        return a+b

print("Sum is : ",student.add(10, 20))
