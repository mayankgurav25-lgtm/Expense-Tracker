import csv
import os

FILENAME = "expenses.csv"

# Ensure the file exists
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Description", "Amount"])  # header

def add_expense(description, amount):
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, amount])
    print("✅ Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.")
        return

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if len(expenses) <= 1:
        print("No expenses recorded yet.")
        return

    print("\n--- Expense List ---")
    total = 0
    for i, row in enumerate(expenses[1:], start=1):
        desc, amt = row
        print(f"{i}. {desc} - ₹{amt}")
        total += float(amt)
    print(f"Total: ₹{total}\n")

def delete_expense(index):
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if index < 1 or index >= len(expenses):
        print("❌ Invalid index!")
        return

    removed = expenses.pop(index)

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

    print(f"🗑️ Removed: {removed[0]} - ₹{removed[1]}")

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            desc = input("Enter description: ")
            amt = input("Enter amount: ")
            add_expense(desc, amt)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_expenses()
            try:
                idx = int(input("Enter expense number to delete: "))
                delete_expense(idx)
            except ValueError:
                print("❌ Please enter a valid number!")
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
