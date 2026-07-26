#Calculating Income Tax 
salary = float(input("Enter your salary: "))
match salary:
    case salary if salary <= 250000:
        print("No Tax")
    case salary if 250001 <= salary <= 500000:
        s1 = salary * 0.05
        print(f"your tax is {s1}")
    case salary if 500001 <= salary <= 1000000:
        print(f"Your tax is {salary * 0.2}")
    case salary if salary> 1000000:
        print(f"Your tax is {salary * 0.3}")
        