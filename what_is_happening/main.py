#Devin Longtree What is Happening?

class BankAccount: #Creating a class for the bank account
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): #Depositing money
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount): #Withdrawing money
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self): #see your balance
        return self.balance

def create_account(): #Creating the account
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))#Inputting your initial balance
    return BankAccount(account_number, initial_balance)

def main(): #Begin the code for the main program
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1': #What happens if you choose 1 (creates account)
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']: #What happens if you choose 2, 3, or 4
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                if choice == '2': #Depositing money
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")#Successful Deposit
                    else:
                        print("Invalid deposit amount.")#unsuccessful Deposit
                elif choice == '3': #Withdrawing money
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")#Successful withdraw
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")#Unsuccessful withdraw
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")#Looking at current balance
            else:
                print("Account not found.")#Invalid account number
        
        elif choice == '5': #What happens if you choose 5
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.") #What happens if you choose any other number

if __name__ == "__main__":#Tells the program to run
    main()