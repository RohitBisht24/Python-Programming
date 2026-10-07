# Write a python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Com. 
# Calculate percentage and grade according to following: 
# Percentage >= 90% : Grade A 
# Percentage >= 80% : Grade B 
# Percentage >= 70% : Grade C 
# Percentage >= 60% : Grade D 
# Percentage >= 40% : Grade E 
# Percentage < 40% : Grade F 

phy = int(input("Enter the Physics marks : "))
chem = int(input("Enter the Chmistry marks : "))
bio = int(input("Enter the Biology marks : "))
maths = int(input("Enter the Mathematics marks : "))
com = int(input("Enter the computer marks : "))

if (phy <= 100 and phy >= 0 and
    chem <= 100 and chem >= 0 and
    bio <= 100 and bio >= 0 and 
    maths <= 100 and maths >= 0 and
    com <= 100 and com >= 0):

    total_marks = phy + chem + bio + maths + com
    print("Tatal Marks : ",total_marks)
    percentange = total_marks / 5
    print("Percentage : ",percentange)

    if(percentange <= 100 and percentange >= 90):
        print("final grades : Grade A")
    if(percentange < 90 and percentange >= 80):
        print("final grades : Grade B")
    if(percentange < 80 and percentange >= 70):
        print("final grades : Grade C")
    if(percentange < 70 and percentange >= 60):
        print("final grades : Grade D")
    if(percentange < 60 and percentange >= 50):
        print("final grades : Grade E")
    if(percentange < 50 and percentange >= 40):
        print("final grades : Fail")

else:

    print("Invalid Marks! Marks should be between 0 and 100.")
