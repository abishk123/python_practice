bill = 0
units = int(input('units : '))
bill_200 = 500
if units > 100 and units <=200:
    bill = (units -100) * 5
    print(bill)
elif units > 200:
    bill = bill_200 + (units-200) * 10
    print(bill)
else:
    print(bill)

