import json
from datetime import datetime


class ExpenseManager:

    def __init__(self, file_name="expense.json"):
        self.file_name = file_name
        self.expenses = []
        self.load_expenses()

    # --------------------------------------------------
    # LOAD EXPENSES FROM JSON FILE
    # --------------------------------------------------

    def load_expenses(self):
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)

                if isinstance(data, list):
                    self.expenses = data
                else:
                    self.expenses = []

        except FileNotFoundError:
            self.expenses = []
            self.save_expenses()

        except json.JSONDecodeError:
            print("Warning: expense.json contains invalid data.")
            self.expenses = []

        except Exception as error:
            print(f"Error while loading expenses: {error}")
            self.expenses = []

    # --------------------------------------------------
    # SAVE EXPENSES TO JSON FILE
    # --------------------------------------------------

    def save_expenses(self):
        try:
            with open(self.file_name, "w") as file:
                json.dump(self.expenses, file, indent=4)

        except Exception as error:
            print(f"Error while saving expenses: {error}")

    # --------------------------------------------------
    # GENERATE NEW EXPENSE ID
    # --------------------------------------------------

    def generate_id(self):

        if not self.expenses:
            return 1

        ids = []

        for expense in self.expenses:
            ids.append(expense["id"])

        return max(ids) + 1

    # --------------------------------------------------
    # ADD EXPENSE
    # --------------------------------------------------

    def add_expense(self, amount, category, description):

        expense = {
            "id": self.generate_id(),
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%d-%m-%Y")
        }

        self.expenses.append(expense)

        self.save_expenses()

    # --------------------------------------------------
    # VIEW ALL EXPENSES
    # --------------------------------------------------

    def view_expenses(self):

        if not self.expenses:
            print("No expenses found.")
            return

        print(
            f"{'ID':<5}"
            f"{'Date':<15}"
            f"{'Category':<15}"
            f"{'Amount':<12}"
            f"Description"
        )

        print("-" * 75)

        for expense in self.expenses:

            print(
                f"{expense['id']:<5}"
                f"{expense['date']:<15}"
                f"{expense['category']:<15}"
                f"₹{expense['amount']:<11.2f}"
                f"{expense['description']}"
            )

    # --------------------------------------------------
    # FIND EXPENSE BY ID
    # --------------------------------------------------

    def find_expense(self, expense_id):

        for expense in self.expenses:

            if expense["id"] == expense_id:
                return expense

        return None

    # --------------------------------------------------
    # UPDATE EXPENSE
    # --------------------------------------------------

    def update_expense(
        self,
        expense_id,
        amount=None,
        category=None,
        description=None
    ):

        expense = self.find_expense(expense_id)

        if expense is None:
            return False

        if amount is not None:
            expense["amount"] = amount

        if category is not None:
            expense["category"] = category

        if description is not None:
            expense["description"] = description

        self.save_expenses()

        return True

    # --------------------------------------------------
    # DELETE EXPENSE
    # --------------------------------------------------

    def delete_expense(self, expense_id):

        expense = self.find_expense(expense_id)

        if expense is None:
            return False

        self.expenses.remove(expense)

        self.save_expenses()

        return True

    # --------------------------------------------------
    # SEARCH BY CATEGORY
    # --------------------------------------------------

    def search_by_category(self, category):

        found_expenses = []

        for expense in self.expenses:

            if expense["category"].lower() == category.lower():
                found_expenses.append(expense)

        self.display_search_results(found_expenses)

    # --------------------------------------------------
    # SEARCH BY DATE
    # --------------------------------------------------

    def search_by_date(self, date):

        try:
            datetime.strptime(date, "%d-%m-%Y")

        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY.")
            return

        found_expenses = []

        for expense in self.expenses:

            if expense["date"] == date:
                found_expenses.append(expense)

        self.display_search_results(found_expenses)

    # --------------------------------------------------
    # SEARCH BY AMOUNT
    # --------------------------------------------------

    def search_by_amount(self, amount):

        found_expenses = []

        for expense in self.expenses:

            if expense["amount"] == amount:
                found_expenses.append(expense)

        self.display_search_results(found_expenses)

    # --------------------------------------------------
    # DISPLAY SEARCH RESULTS
    # --------------------------------------------------

    def display_search_results(self, expenses):

        if not expenses:
            print("\nNo matching expenses found.")
            return

        print(
            f"\n{'ID':<5}"
            f"{'Date':<15}"
            f"{'Category':<15}"
            f"{'Amount':<12}"
            f"Description"
        )

        print("-" * 75)

        for expense in expenses:

            print(
                f"{expense['id']:<5}"
                f"{expense['date']:<15}"
                f"{expense['category']:<15}"
                f"₹{expense['amount']:<11.2f}"
                f"{expense['description']}"
            )

    # --------------------------------------------------
    # CALCULATE TOTAL EXPENSE
    # --------------------------------------------------

    def get_total_expense(self):

        total = 0

        for expense in self.expenses:
            total += expense["amount"]

        return total

    # --------------------------------------------------
    # CATEGORY-WISE REPORT
    # --------------------------------------------------

    def category_report(self):

        if not self.expenses:
            print("No expenses found.")
            return

        category_totals = {}

        for expense in self.expenses:

            category = expense["category"]
            amount = expense["amount"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        print(
            f"{'Category':<20}"
            f"{'Total Expense':<15}"
        )

        print("-" * 35)

        for category, total in category_totals.items():

            print(
                f"{category:<20}"
                f"₹{total:.2f}"
            )

        print("-" * 35)

        print(
            f"{'Grand Total':<20}"
            f"₹{self.get_total_expense():.2f}"
        )
