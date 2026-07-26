#Simple calculator using switch 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
Op = int(input("\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Modulus \nEnter your choice:  "))
match Op:
    case Op if Op == 1:
        print(f"Addition of {num1} and {num2} is {num1 + num2}")
    case Op if Op == 2:
        print(f"Subtraction of {num1} and {num2} is {num1 - num2}")
    case Op if Op == 3:
        print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
    case Op if Op == 4:
        print(f"Division of {num1} and {num2} is {num1 / num2}")
    case Op if Op ==5: 
        print(f"Modulus of {num1} and {num2} is {num1 % num2}")
    case Op if Op < 1 or Op > 5:
        print("Invalid choice")