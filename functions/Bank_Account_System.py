def create_account():

    name = input("Enter your name. : ")
    acc_num = int(input("Enter your account number. : "))
    balance = float(input("Enter your initial balance. : "))

    return name , acc_num , balance

def deposit(balance):
    amount = float(input("Enter the amount you want to deposit. : "))

    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully.")
    else:
        print("Invalid amount!")

    return balance

def withdraw(balance):

    withdrawn = float(input("Enter the amount you want to withdraw. : "))

    if withdrawn <= 0:
        print("Invalid amount.")
    elif withdrawn > balance:
        print("Insufficient balance")
    else:
        balance = balance - withdrawn
        print("Amount withdrawn successfully.")

        return balance 

def check_balance(balance):
    print("Current balance is = " , balance)



def display_account(name , acc_num , balance):
    print("\n--------------- ACCOUNT DETAILS ---------------")
    print("Name of account holder is : ", name)
    print("Account number is : " , acc_num)
    print("Balance is : ₹" , balance)


def menu(name, acc_num , balance):

        print("\n----------BANK MENU----------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. check balance")
        print("4. Display all Details")
        print("5. Exit")

        while True:
            choice = int(input("Enter your choice : "))
        
            match choice:
                case 1: 
                    balance = deposit(balance)
        
                case 2: 
                    balance = withdraw(balance)
        
                case 3:
                    check_balance(balance)
        
                case 4: 
                    display_account(name , acc_num , balance)
        
                case 5:
                    print("Thank you for using our bank.")
                    break
        
                case _: 
                    print("Aree pagal hai kya !")

        return balance


# Function call

name, acc_num, balance = create_account()
balance = menu(name, acc_num , balance)