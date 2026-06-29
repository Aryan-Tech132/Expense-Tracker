import csv
import os
from datetime import datetime


# Function to Add Expense
def add_expense():

    while True:
        date = input("Enter Date (DD-MM-YYYY): ")

        try:
            datetime.strptime(date, "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid Date! Please use DD-MM-YYYY format.")

    category = input("Enter Category: ")

    while True:
        try:
            amount = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Please enter a valid amount.")

    file_exists = os.path.exists("expenses.csv")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Amount"])

        writer.writerow([date, category, amount])

    print("\nExpense Added Successfully!\n")


# Function to View Expenses
def view_expenses():

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            print("\n{:<15}{:<20}{:<10}".format("Date", "Category", "Amount"))
            print("-" * 45)

            next(reader)  # Skip Header

            for row in reader:
                print("{:<15}{:<20}{:<10}".format(row[0], row[1], row[2]))

    except FileNotFoundError:
        print("\nNo Expenses Found!\n")


# Function to Calculate Total Expense
def calculate_total():

    total = 0

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            next(reader)  # Skip Header

            for row in reader:
                total += float(row[2])

        print(f"\nTotal Expense: ₹{total:.2f}\n")

    except FileNotFoundError:
        print("\nNo Expenses Found!\n")


# Main Menu
def main():

    while True:

        print("=" * 35)
        print("      EXPENSE TRACKER")
        print("=" * 35)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            print("\nThank You for Using Expense Tracker!")
            break

        else:
            print("\nInvalid Choice! Please Try Again.\n")


if __name__ == "__main__":
    main()