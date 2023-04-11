#  ______ _                              __  __                                   
# |  ____(_)                            |  \/  |                                  
# | |__   _ _ __   __ _ _ __   ___ ___  | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
# |  __| | | '_ \ / _` | '_ \ / __/ _ \ | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
# | |    | | | | | (_| | | | | (_|  __/ | |  | | (_| | | | | (_| | (_| |  __/ |   
# |_|    |_|_| |_|\__,_|_| |_|\___\___| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
#                                                                  __/ |          
#                                                                 |___/           
# By A.S.

# The following program is a Finance Management System.
# It works through the console by following predetermined instructions.
# The instructions are labeled from 1 to 6 and do the following:
#   1. Add income: Adds an income, a positive number to your balance.
#   2. Add expenditure: Adds an expenditure, a negative number to your balance.
#   3. Show balance: Prints the sum of the incomes minus the sum of the expenditures.
#   4. Show incomes: Prints all of the incomes
#   5. Show expenditures: Prints all of the expenditures
#   6. Exit: quits the program

class Transaction:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def __str__(self):
        return "{}: ${:.2f}".format(self.name, self.amount)

class FinanceManager:
    def __init__(self):
        self.incomes = []
        self.expenditures = []
    
    def add_income(self, name, amount):
        self.incomes.append(Transaction(name, amount))
    
    def add_expenditure(self, name, amount):
        self.expenditures.append(Transaction(name, amount))
    
    def calculate_balance(self):
        total_income = sum(t.amount for t in self.incomes)
        total_expenditure = sum(t.amount for t in self.expenditures)
        return total_income - total_expenditure
    
    def display_transactions(self, transactions):
        for i, t in enumerate(transactions):
            print("{}. {}".format(i+1, t))
    
finance_manager = FinanceManager()

while True:
    print("1. Add Income")
    print("2. Add Expenditure")
    print("3. Show Balance")
    print("4. Show Incomes")
    print("5. Show Expenditures")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter the name of the income: ")
        amount = float(input("Enter the amount: "))
        finance_manager.add_income(name, amount)
        print("Income added successfully.")
    elif choice == 2:
        name = input("Enter the name of the expenditure: ")
        amount = float(input("Enter the amount: "))
        finance_manager.add_expenditure(name, amount)
        print("Expenditure added successfully.")
    elif choice == 3:
        balance = finance_manager.calculate_balance()
        if balance >= 0:
            print("You are winning money. Balance: ${:.2f}".format(balance))
        else:
            print("You are losing money. Balance: ${:.2f}".format(balance))
    elif choice == 4:
        finance_manager.display_transactions(finance_manager.incomes)
    elif choice == 5:
        finance_manager.display_transactions(finance_manager.expenditures)
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")
