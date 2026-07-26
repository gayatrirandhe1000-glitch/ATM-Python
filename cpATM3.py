#Write a program to create a ATM machine
print("Welcome to GSR ATM")
balance = int(input("Enter your initial balance: "))
current_pin = 1234  # Set a default pin for the ATM

def withdraw():
    global balance
    if balance <= 1000:
        print("Insufficient Balance")
    else:
        amount = int(input("Enter the amount to withdraw: "))
        pin()
        if amount > 0 and amount <= balance:
            print("Amount Withdrawn Successfully!\n")
            balance = balance - amount
            print(f"Your Current Balance is {balance}\n \n")
        else:
            print("Invalid Amount or Insufficient Balance\n \n")
    atm()

def depo():
    global balance
    amount = int(input("Enter the amount to deposite: "))
    pin()
    if amount >0 :
        print("Amount Deposited Successfully!\n")
        balance = balance + amount
        print(f"Your Current Balance is {balance}\n \n ")
    else:
        print("Invalid Amount\n \n")
    atm()

def check_balance():
    global balance
    pin()
    print(f"Your Current Balance is {balance}\n \n ")
    return balance
    atm()

def pin():
    attempts = 3
    while attempts > 0:
        pin = int(input("Enter Your 4 digit pin: \n"))
        if pin == current_pin:
            print("Pin Matched")
            break
        else:
            attempts -= 1
            print(f"Incorrect Pin. You have {attempts} attempts left.")
    else:
        print("You have exceeded the maximum number of attempts. Please try again later.\n \n ")
        quit()

def new_pin():
    global current_pin
    pin = int(input("Enter your current pin: \n"))
    if pin == current_pin:
        new_pin = int(input("Enter your new 4 digit pin: \n"))
        confirm_pin = int(input("Confirm your new pin: \n"))
        if new_pin == confirm_pin:
            current_pin = new_pin
            print("Pin changed successfully! \n \n")
        else:
            print("Pin confirmation does not match. Please try again. \n \n")
    else:
        print("Incorrect current pin. Please try again. \n \n")
    atm()

def exit():
    quit()

def atm():
    while True:
        choice = int(input("\n1. Withdraw\n2. Deposite\n3. Check Balance\n4. Change pin\n5. Exit\nEnter your desired Option Number: "))
        match choice :
            case choice if choice<1 and choice>5 :
                print("Invalid Choice")
            case choice if choice == 1:
                print("\nWithdraw")
                withdraw()
            case choice if choice == 2:
                print("\nDeposite")
                depo()
            case choice if choice ==3:
                print("\nCheck Balance")
                check_balance()
            case choice if choice == 4:
                print("\nPin Change")
                new_pin()
            case choice if choice ==5:
                print("\nThank you for using our ATM!") 
                exit()
atm()