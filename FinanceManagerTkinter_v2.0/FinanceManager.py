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

        # Incomes listbox
        self.incomes_listbox = tk.Listbox(self.window)
        self.incomes_listbox.grid(row=2, column=0, padx=10, pady=10)
        self.incomes_listbox.bind('<Double-Button-1>', self.edit_income)

        # Expenditures listbox
        self.expenditures_listbox = tk.Listbox(self.window)
        self.expenditures_listbox.grid(row=2, column=1, padx=10, pady=10)
        self.expenditures_listbox.bind('<Double-Button-1>', self.edit_expenditure)

        # Exit button
        exit_button = ttk.Button(
            self.window, text="Exit", command=self.window.quit)
        exit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # (The rest of the methods remain the same)

    def add_income(self):
        dialog = AddTransactionDialog(self.window, "Add Income", "income")
        self.window.wait_window(dialog)

        if dialog.name and dialog.amount is not None:
            self.finance_manager.add_income(dialog.name, dialog.amount)
            messagebox.showinfo("Success", "Income added successfully.")
            self.update_incomes_listbox()


    def add_expenditure(self):
        dialog = AddTransactionDialog(self.window, "Add Expenditure", "expenditure")
        self.window.wait_window(dialog)

        if dialog.name and dialog.amount is not None:
            self.finance_manager.add_expenditure(dialog.name, dialog.amount)
            messagebox.showinfo("Success", "Expenditure added successfully.")
            self.update_expenditures_listbox()

    def edit_income(self, event):
        index = self.incomes_listbox.curselection()[0]
        income = self.finance_manager.incomes[index]

        new_name = self.get_name(f"Edit the name of the income (current: {income.name}):")
        if new_name:
            income.name = new_name

        new_amount = self.get_amount(f"Edit the amount (current: {income.amount}):")
        if new_amount is not None:
            income.amount = new_amount

        self.update_incomes_listbox()

    def edit_expenditure(self, event):
        index = self.expenditures_listbox.curselection()[0]
        expenditure = self.finance_manager.expenditures[index]

        new_name = self.get_name(f"Edit the name of the expenditure (current: {expenditure.name}):")
        if new_name:
            expenditure.name = new_name

        new_amount = self.get_amount(f"Edit the amount (current: {expenditure.amount}):")
        if new_amount is not None:
            expenditure.amount = new_amount

        self.update_expenditures_listbox()
    
    def show_balance(self):
        balance = self.finance_manager.calculate_balance()
        if balance >= 0:
            messagebox.showinfo("Balance", "You are winning money. Balance: ${:.2f}".format(balance))
        else:
            messagebox.showinfo("Balance", "You are losing money. Balance: ${:.2f}".format(balance))

    def update_incomes_listbox(self):
        self.incomes_listbox.delete(0, tk.END)
        for income in self.finance_manager.incomes:
            self.incomes_listbox.insert(tk.END, str(income))

    def update_expenditures_listbox(self):
        self.expenditures_listbox.delete(0, tk.END)
        for expenditure in self.finance_manager.expenditures:
            self.expenditures_listbox.insert(tk.END, str(expenditure))

    def run(self):
        self.window.mainloop()

class AddTransactionDialog(tk.Toplevel):
    def __init__(self, parent, title, transaction_type):
        super().__init__(parent)
        self.title(title)
        self.transaction_type = transaction_type
        self.name = None
        self.amount = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Amount:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        buttons_frame = tk.Frame(self)
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=5)

        add_button = ttk.Button(buttons_frame, text="Add", command=self.add_transaction)
        add_button.pack(side="left", padx=5)

        cancel_button = ttk.Button(buttons_frame, text="Cancel", command=self.destroy)
        cancel_button.pack(side="left", padx=5)

    def add_transaction(self):
        self.name = self.name_entry.get()
        try:
            self.amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return

        self.destroy()

if __name__ == "__main__":
    finance_manager = FinanceManager()
    app = FinanceManagerGUI(finance_manager)
    app.run()

           
