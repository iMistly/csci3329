class Account:
    def __init__(self, name:str, password:str) -> int:
        self.name = name
        self.password = password
        self.balance:float = 0
        self.transactions = ["Account Created"]

    def deposit(self, amnt:float) -> None:
        self.balance += amnt
        self.transactions.append(f"Deposit: ${amnt:,.2f}, Balance: ${self.balance:,.2f}")
    
    def withdraw(self, amnt:float) -> None:
        inputValid = True
        if(self.balance == 0):
            print("You do not own a penny!")
            return -1
        while(not(0 < amnt and amnt <= self.balance)):
            if (inputValid):
                print(f"You cannot withdraw ${amnt:,.2f}")
            try:
                amnt = float(input("How much would you like to withdraw?: "))
                inputValid = True
            except:
                print("That is an invalid number!")
                inputValid = False
        self.transactions.append(f"Withdraw: ${amnt:,.2f}, Balance: ${self.balance:,.2f}")
        
    def display(self) -> None:
        print(f"You have ${self.balance:,.2f}")
        
    def history(self) -> None:
        print("\nHistory:")
        for x in self.transactions:
            print(x)
        print()
            
class Bank:
    def __init__(self) -> None:
        self.accounts:Account = []
    
    def createAccount(self) -> None:
        name = input("Name your account: ")
        password = input(f"Secure '{name}' with a password: ")
        self.accounts.append(Account(name, password))
        
    def closeAccount(self) -> None:
        if(len(self.accounts) == 0):
            print("No accounts to remove")
            return -1
        
        inputValid = False
        index = 0
        while(not(inputValid)):
            name = input("What is the name of the account you would like to close: ")
            for x in self.accounts:
                if(x.name == name):
                    inputValid = True
                    break
                index += 1
            print(f"'{name}' does not exist")
            index = 0
            
        password = ""
        while(not(password == self.accounts[index].password)):
            password = input(f"Verify password for '{name}': ")
        
        verify = ""
        while(verify in ['y', 'n']):
            verify = input(f"Are you sure you want to delete '{name}'?: ").lower()
            print(verify)
        
        if(verify == "y"):
            self.accounts.pop(index)
        else:
            print(f"Aborted deletion of '{name}'")
                
    
    
newBank = Bank()
newBank.createAccount()
newBank.accounts[0].display()
newBank.closeAccount()