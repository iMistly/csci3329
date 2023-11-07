#Lists available options and asks the user to pick
def listChoices():
    choice = 0
    print("\nWhat would you like to do with your account?")
    print("\t1. Deposit")
    print("\t2. Withdraw")
    print("\t3. Display balance")
    print("\t4. Exit")
    while(not(1 <= choice and choice <= 4)):
        try:
            choice = int(input("Choose an option 1-4: "))
            if(not(1 <= choice and choice <= 4)):
                print(f"{choice} is not a valid option...")
        except:
            print("That is an invalid number!")
    print()
    return choice

#Asks user to make a deposit, does not add deposit to inBalance
def deposit(inBalance):
    deposit = 0.0
    while(deposit <= 0):
        try:
            deposit = float(input("How much would you like to deposit?: "))
            if(deposit <= 0):
                print("You must deposit at least 1 cent...")
        except:
            print("That is an invalid number!")
    print(f"Your new balance is ${inBalance + deposit:,.2f}")
    return deposit

#Asks user to make a withdrawal, does not remove withdrawal from inBalance
def withdraw(inBalance):
    withdrawal = 0.0
    if(inBalance == 0):
        print("You do not own a penny!")
        return 0
    print(f"You have ${inBalance:,.2f}.")
    while(not(0 < withdrawal and withdrawal <= inBalance)):
        try:
            withdrawal = float(input("How much would you like to withdraw?: "))
            if(withdrawal <= 0):
                print("You must withdraw at least 1 cent")
            elif(withdrawal > inBalance):
                print(f"You only have ${inBalance:,.2f}")
        except:
            print("That is an invalid number!")
    print(f"Your new balance is ${inBalance - withdrawal:,.2f}")
    return withdrawal

myBalance = deposit(0)
choice = listChoices()

while(choice != 4):
    if(choice == 1):
        myBalance += deposit(myBalance)
    elif(choice == 2):
        myBalance -= withdraw(myBalance)
    else:
        print(f"Your current balance is ${myBalance:,.2f}")
    choice = listChoices()