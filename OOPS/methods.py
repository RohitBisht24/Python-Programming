class student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age =  age
        
    # method
    def hello(self):
        print("Hello student.", self.name)

    # method
    def get_marks(self):
        return self.marks

s1 = student("karan", 21)
s1.hello()
print(s1.get_marks)


