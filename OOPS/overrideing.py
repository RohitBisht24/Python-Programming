class Employee:
    def get_desgnation(self):
        print("designaltion = Employee")

class Teacher(Employee):
    def get_desgnation(self):
        print("designaltion = Teacher")

t1 = Teacher()
t1.get_desgnation()
