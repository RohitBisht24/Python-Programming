year = int(input("Enter the year : "))

if year % 100 == 0 and year % 400 == 0:
    print("leap year.")
elif year % 100 != 0 and year % 4 == 0:
    print("Leap year.")
else:
    print("Not a leap year.")
