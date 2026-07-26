#Write a program to calculate the electricity bill on basis of units. first 100 units Rs. 5/unit, next 100 units Rs. 7/unit, above 200 units Rs. 10/unit.
units = int(input("Enter the number of units consumed:"))
if units <=100:
    billat_5 = units * 5
    print(f"Electricity bill for first {units} units is Rs. {billat_5}")
elif units <= 200:
    billat_5 = 100*5
    billat_7 = (units - 100) *7
    total_bill = billat_5 + billat_7
    print(f"Electricity bill for first 100 units is Rs. {billat_5} and for next {units-100} units is Rs. {billat_7}. Total bill is Rs. {total_bill}")
else:
    billat_5 =100*5
    billat_7 = (units - 100) *7
    billat_10 = (units - 200) *10
    total_bill = billat_5 + billat_7 + billat_10
    print(f"Electricity bill for first 100 units is Rs. {billat_5}, for next 100 units is Rs. {billat_7}, and for units above 200 is Rs. {billat_10}. Total bill is Rs. {total_bill}")