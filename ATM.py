#Write a program to create a ATM machine
print("Welcome to GSR ATM")
balance = int(input("Enter your initial balance: "))

def withdraw(balance):
    if balance <= 1000:
        print("Insufficient Balance")
    else:
        amount = int(input("Enter the amount to withdraw: "))
        print("Amount Withdrawn Successfully!\n")
        balance = balance- amount
        print(f"Your Current Balance is {balance}")
    return balance 
    atm()

def depo(balance):

    amount = int(input("Enter the amount to deposite: "))
    if amount >0 :
        print("Amount Deposited Successfully!\n")
        balance = balance + amount
        print(f"Your Current Balance is {balance}")
        return balance
    else:
        print("Invalid Amount")
    atm()

def check_balance(balance):
    print(f"Your Current Balance is {balance}")
    return balance
    atm()


def atm(balance):
    while True:
        choice = int(input("1. Withdraw\n2. Deposite\n3. Check Balance\n4. Change pin\n5. Exit\nEnter your desired Option Number: "))
        match choice :
            case choice if choice<1 and choice>5 :
                print("Invalid Choice")
            case choice if choice == 1:
                print("Withdraw")
                withdraw(balance)
            case choice if choice == 2:
                print("Deposite")
                depo(balance)
            case choice if choice ==3:
                print("Check Balance")
                check_balance(balance)
            case choice if choice == 4:
                print("Pin Change")
            case choice if choice ==5:
                print("Exit") 
atm(balance)