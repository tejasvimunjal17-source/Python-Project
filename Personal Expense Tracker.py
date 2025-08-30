#Python Programming Mini Project: "Personal Expense Tracker"

import json
import os
from datetime import datetime

# file to save our expenses
filename = "expenses.json"

# function to load previous expenses
def load_expenses():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        return []   # no file yet, return empty list

# function to save expenses into file
def save_expenses(exp_list):
    with open(filename, "w") as f:
        json.dump(exp_list, f, indent=4)

# function to add a new expense
def add_expense(exp_list):
    try:
        amt = float(input("Enter amount: $"))
        cat = input("Enter category (Food, Travel, etc): ")
        date_in = input("Enter date (YYYY-MM-DD) or press enter for today: ")

        if date_in.strip() == "":
            date_in = datetime.now().strftime("%Y-%m-%d")

        expense = {"amount": amt, "category": cat, "date": date_in}
        exp_list.append(expense)
        save_expenses(exp_list)
        print("Expense saved!\n")

    except:
        print("Invalid amount. Please enter numbers only.\n")

# function to view summary
def view_summary(exp_list):
    if len(exp_list) == 0:
        print("No expenses found yet.\n")
        return

    total = 0
    cat_summary = {}
    date_summary = {}

    for e in exp_list:
        total += e["amount"]
        # category wise
        if e["category"] in cat_summary:
            cat_summary[e["category"]] += e["amount"]
        else:
            cat_summary[e["category"]] = e["amount"]
        # date wise
        if e["date"] in date_summary:
            date_summary[e["date"]] += e["amount"]
        else:
            date_summary[e["date"]] = e["amount"]

    print("=== Expense Summary ===")
    print("Total spent: $", total)

    print("\nBy Category:")
    for c in cat_summary:
        print(c, ":", cat_summary[c])

    print("\nBy Date:")
    for d in date_summary:
        print(d, ":", date_summary[d])
    print()

# main program loop
def main():
    expenses = load_expenses()

    while True:
        print("----- Personal Expense Tracker -----")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            add_expense(expenses)
        elif ch == "2":
            view_summary(expenses)
        elif ch == "3":
            print("Exiting... Bye!")
            break
        else:
            print("Wrong choice, try again.\n")

if __name__ == "__main__":
    main()

    #Submitted By - Tejasvi Munjal
    #Mobile No. - +91 7982602495
    #Email Address - tejasvimunjal17@gmail.com
                                                #Submitted To - Vault of Code
