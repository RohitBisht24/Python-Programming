from expense_manager import ExpenseManager


def display_menu():
    print("\n" + "=" * 45)
    print("           EXPENSE TRACKER")
    print("=" * 45)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search Expenses")
    print("6. Show Total Expense")
    print("7. Category-wise Report")
    print("8. Exit")
    print("=" * 45)


def add_expense(manager):
    print("\n---------- ADD EXPENSE ----------")

    try:
        amount = float(input("Enter amount: ").strip())

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        category = input("Enter category: ").strip()

        if not category:
            print("Category cannot be empty.")
            return

        description = input("Enter description: ").strip()

        manager.add_expense(amount, category, description)

        print("\nExpense added successfully!")

    except ValueError:
        print("\nInvalid amount. Please enter a valid number.")


def view_expenses(manager):
    print("\n---------- ALL EXPENSES ----------")
    manager.view_expenses()


def update_expense(manager):
    print("\n---------- UPDATE EXPENSE ----------")

    try:
        expense_id = int(input("Enter Expense ID: ").strip())

        amount_input = input(
            "Enter new amount (press Enter to keep old amount): "
        ).strip()

        if amount_input:
            amount = float(amount_input)

            if amount <= 0:
                print("Amount must be greater than 0.")
                return
        else:
            amount = None

        category = input(
            "Enter new category (press Enter to keep old category): "
        ).strip()

        if not category:
            category = None

        description = input(
            "Enter new description (press Enter to keep old description): "
        ).strip()

        if not description:
            description = None

        updated = manager.update_expense(
            expense_id,
            amount,
            category,
            description
        )

        if updated:
            print("\nExpense updated successfully!")
        else:
            print("\nExpense ID not found.")

    except ValueError:
        print("\nInvalid input. Please enter a valid value.")


def delete_expense(manager):
    print("\n---------- DELETE EXPENSE ----------")

    try:
        expense_id = int(input("Enter Expense ID: ").strip())

        deleted = manager.delete_expense(expense_id)

        if deleted:
            print("\nExpense deleted successfully!")
        else:
            print("\nExpense ID not found.")

    except ValueError:
        print("\nInvalid Expense ID. Please enter a number.")


def search_expenses(manager):
    print("\n---------- SEARCH EXPENSES ----------")
    print("1. Search by Category")
    print("2. Search by Date")
    print("3. Search by Amount")
    print("4. Back")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        category = input("Enter category: ").strip()

        if not category:
            print("Category cannot be empty.")
            return

        manager.search_by_category(category)

    elif choice == "2":
        date = input("Enter date (DD-MM-YYYY): ").strip()

        if not date:
            print("Date cannot be empty.")
            return

        manager.search_by_date(date)

    elif choice == "3":
        try:
            amount = float(input("Enter amount: ").strip())

            if amount <= 0:
                print("Amount must be greater than 0.")
                return

            manager.search_by_amount(amount)

        except ValueError:
            print("Invalid amount.")

    elif choice == "4":
        return

    else:
        print("Invalid choice.")


def show_total_expense(manager):
    print("\n---------- TOTAL EXPENSE ----------")

    total = manager.get_total_expense()

    print(f"Total Expense: ₹{total:.2f}")


def show_category_report(manager):
    print("\n---------- CATEGORY-WISE REPORT ----------")

    manager.category_report()


def main():
    manager = ExpenseManager()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(manager)

        elif choice == "2":
            view_expenses(manager)

        elif choice == "3":
            update_expense(manager)

        elif choice == "4":
            delete_expense(manager)

        elif choice == "5":
            search_expenses(manager)

        elif choice == "6":
            show_total_expense(manager)

        elif choice == "7":
            show_category_report(manager)

        elif choice == "8":
            print("\nThank you for using Expense Tracker!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()