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
# The difference from v1.0 is that it is able to store data even if you quit.
# The instructions are labeled from 1 to 6 and do the following:
#   1. Add income: Adds an income, a positive number to your balance.
#   2. Add expenditure: Adds an expenditure, a negative number to your balance.
#   3. Show balance: Prints the sum of the incomes minus the sum of the expenditures.
#   4. Show incomes: Prints all of the incomes.
#   5. Show expenditures: Prints all of the expenditures.
#   7. Save data: saves the incomes and expenses on an exterior file.
#   8. Load data: loads the incomes and expenses from an exterior file.
#   6. Exit: quits the program.

import json

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
    
    def save_data(self, filename):
        data = {
            "incomes": [t.__dict__ for t in self.incomes],
            "expenditures": [t.__dict__ for t in self.expenditures]
        }
        with open(filename, "w") as f:
            json.dump(data, f)
    
    def load_data(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.incomes = [Transaction(t["name"], t["amount"]) for t in data["incomes"]]
                self.expenditures = [Transaction(t["name"], t["amount"]) for t in data["expenditures"]]
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Invalid JSON format.")
        except Exception as e:
            print("Error loading data:", str(e))

finance_manager = FinanceManager()

while True:
    print("1. Add Income")
    print("2. Add Expenditure")
    print("3. Show Balance")
    print("4. Show Incomes")
    print("5. Show Expenditures")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if choice == 1:
        name = input("Enter the name of the income: ")
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid input. Amount must be a number.")
            continue
        finance_manager.add_income(name, amount)
        print("Income added successfully.")
    elif choice == 2:
        name = input("Enter the name of the expenditure: ")
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid input. Amount must be a number.")
            continue
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
        filename = input("Enter the filename: ")
        finance_manager.save_data(filename)
        print("Data saved successfully.")
    elif choice == 7:
        filename = input("Enter the filename: ")
        finance_manager.load_data(filename)
        print("Data loaded successfully.")
    elif choice == 8:
        break
    else:
        print("Invalid choice. Please try again.")

