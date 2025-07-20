import csv
import os
import datetime

FILE_NAME = "expenses.csv"
FIELDNAMES = ["date", "amount", "category", "description"]

def load_expenses():
    expenses = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    return expenses

def save_expenses(expenses):
    with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)

def add_expense(expenses):
    try:
        amount = float(input("Enter amount (₺): "))
        category = input("Enter category (e.g., food, rent): ").strip()
        description = input("Enter description: ").strip()
        date = input("Enter date (YYYY-MM-DD) [leave blank for today]: ").strip()
        if date == "":
            date = str(datetime.date.today())
        else:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        expenses.append({
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        })
        save_expenses(expenses)
        print("Expense added successfully.\n")
    except ValueError:
        print("Invalid input. Please try again.\n")

def show_expenses(expenses):
    if not expenses:
        print("No expenses found.\n")
        return
    expenses_sorted = sorted(expenses, key=lambda x: x["date"])
    print("\nAll Expenses:\n")
    print("{:<5} {:<12} {:<10} {:<10} {}".format("No", "Date", "Amount", "Category", "Description"))
    print("-" * 60)
    for i, exp in enumerate(expenses_sorted, 1):
        print("{:<5} {:<12} {:<10.2f} {:<10} {}".format(i, exp["date"], exp["amount"], exp["category"], exp["description"]))
    print()

def total_spent(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Spent: ₺{total:.2f}\n")

def filter_by_category(expenses):
    cat = input("Enter category to filter: ").strip().lower()
    filtered = [exp for exp in expenses if exp["category"].lower() == cat]
    if not filtered:
        print(f"No expenses found for category: {cat}\n")
    else:
        print(f"\nExpenses in category '{cat}':\n")
        for exp in filtered:
            print(f"{exp['date']} | ₺{exp['amount']} | {exp['description']}")
        print()

def delete_expense(expenses):
    show_expenses(expenses)
    try:
        index = int(input("Enter the number of the expense to delete (0 to cancel): "))
        if index == 0:
            print("Deletion cancelled.\n")
            return
        if 1 <= index <= len(expenses):
            deleted = expenses.pop(index - 1)
            save_expenses(expenses)
            print(f"Deleted: ₺{deleted['amount']} - {deleted['category']} - {deleted['description']}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def show_menu():
    print("======== PERSONAL EXPENSE TRACKER ========")
    print("1. Add Expense")
    print("2. Show All Expenses")
    print("3. Show Total Spent")
    print("4. Filter by Category")
    print("5. Delete an Expense")
    print("6. Exit")
    print("==========================================")

def main():
    expenses = load_expenses()
    while True:
        show_menu()
        choice = input("Select an option (1-6): ").strip()
        print()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            total_spent(expenses)
        elif choice == "4":
            filter_by_category(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.\n")

if __name__ == "__main__":
    main()
