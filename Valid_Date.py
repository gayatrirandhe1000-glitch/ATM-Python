#Check if the entered date is valid or not
from datetime import datetime
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
try:
    d = date(year, month, day)
    print(f"The entered date {day}/{month}/{year} is valid.")
except ValueError:
    print(f"The entered date {day}/{month}/{year} is invalid.")
