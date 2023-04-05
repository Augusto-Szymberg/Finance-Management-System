import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


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
        return '\n'.join("{}. {}".format(i + 1, t) for i, t in enumerate(transactions))


class FinanceManagerGUI:
    def __init__(self, finance_manager):
        self.finance_manager = finance_manager
        self.window = tk.Tk()
        self.window.title("Finance Manager")

        self.create_widgets()

    def create_widgets(self):
        # Add Income button
        add_income_button = ttk.Button(
            self.window, text="Add Income", command=self.add_income)
        add_income_button.grid(row=0, column=0, padx=10, pady=10)

        # Add Expenditure button
        add_expenditure_button = ttk.Button(
            self.window, text="Add Expenditure", command=self.add_expenditure)
        add_expenditure_button.grid(row=0, column=1, padx=10, pady=10)

        # Show Balance button
        show_balance_button = ttk.Button(
            self.window, text="Show Balance", command=self.show_balance)
        show_balance_button.grid(row=1, column=0, padx=10, pady=10)

        # Show Incomes button
        show_incomes_button = ttk.Button(
            self.window, text="Show Incomes", command=self.show_incomes)
        show_incomes_button.grid(row=1, column=1, padx=10, pady=10)

        # Show Expenditures button
        show_expenditures_button = ttk.Button(
            self.window, text="Show Expenditures", command=self.show_expenditures)
        show_expenditures_button.grid(row=2, column=0, padx=10, pady=10)

        # Exit button
        exit_button = ttk.Button(
            self.window, text="Exit", command=self.window.quit)
        exit_button.grid(row=2, column=1, padx=10, pady=10)

    def add_income(self):
        name = self.get_name("Enter the name of the income:")
        if name:
            amount = self.get_amount("Enter the amount:")
            if amount is not None:
                self.finance_manager.add_income(name, amount)
                messagebox.showinfo("Success", "Income added successfully.")

    def add_expenditure(self):
        name = self.get_name("Enter the name of the expenditure:")
        if name:
            amount = self.get_amount("Enter the amount:")
            if amount is not None:
                self.finance_manager.add_expenditure(name, amount)
                messagebox.showinfo("Success", "Expenditure added successfully.")

    def show_balance(self):
        balance = self.finance_manager.calculate_balance()
        if balance >= 0:
            messagebox.showinfo("Balance", "You are winning money. Balance: ${:.2f}".format(balance))
        else:
            messagebox.showinfo("Balance", "You are losing money. Balance: ${:.2f}".format(balance))

    def show_incomes(self):
        incomes = self.finance_manager.display_transactions(self.finance_manager.incomes)
        messagebox.showinfo("Incomes", incomes)

    def show_expenditures(self):
        expenditures = self.finance_manager.display_transactions(self.finance_manager.expenditures)
        messagebox.showinfo("Expenditures", expenditures)

    def get_name(self, prompt):
        return simpledialog.askstring("Input", prompt, parent=self.window)

    def get_amount(self, prompt):
        return simpledialog.askfloat("Input", prompt, parent=self.window)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    finance_manager = FinanceManager()
    app = FinanceManagerGUI(finance_manager)
    app.run()
