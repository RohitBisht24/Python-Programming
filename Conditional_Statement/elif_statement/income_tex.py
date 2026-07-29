income = int(input("Enter your income"))
if income <= 250000:
    total_tax = 0
elif income>250000 and income<=500000:
    taxableincome = income-250000
    total_tax = taxableincome*0.05
elif income>=500001 and income<=1000000:
    taxableincome = income-500000
    tax1=(taxableincome/100)*10
    total_tax= tax1+12500
elif income>=1000001 and income<=2000000:
    taxableincome = income-1000000
    tax1=(taxableincome/100)*20
    total_tax= tax1+12500+50000
elif income>=2000001 and income<=3000000:
    taxableincome = income-2000000
    tax1=(taxableincome/100)*30
    total_tax= tax1+12500+50000+200000
elif income>=3000001 :
    taxableincome = income-3000000
    tax1=(taxableincome/100)*40
    total_tax= tax1+12500+50000+200000+300000
print("Payable tax: ", total_tax)