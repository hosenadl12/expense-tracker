import os
import json
import csv
from datetime import datetime
from collections import defaultdict


class ExpenseTracker:
    def __init__(self, data_file='data/expenses.json'):

        # This sets where we want to save expenses
        self.data_file = data_file
        self.expenses = [] # We'll store expenses as a list of dicts
        self._load_expenses() # Load data from file at initialization

    def _load_expenses(self):
        # Load expenses from disk (JSON).
        #If file or folder doesn’t exist, create them and start fresh.

        if not os.path.exists(self.data_file):
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            self._save_expenses([]) # write an empty list to start with

        try:
            with open(self.data_file, 'r') as f:
                self.expenses = json.load(f)
        except json.JSONDecodeError:

        # Handle edge case: file exists but is empty or broken
            self.expenses = []

    def _save_expenses(self, expenses=None):
        # Save expenses to file. If no list is passed in
        # Just use the current self.expenses list.
        if expenses is None:
            expenses = self.expenses
        with open(self.data_file, 'w') as f:
            json.dump(expenses, f, indent=2)

    def add_expense(self, category, amount, date=None):
        # Add a new expense with category, amount, and date.
        # If no date is provided, we default to today.
        date = date or datetime.now().strftime('%Y-%m-%d')
        entry = {'category': category, 'amount': round(amount, 2), 'date': date}
        self.expenses.append(entry)
        self._save_expenses()

    def delete_last_expense(self):
        # Remove the most recent expense (last in the list).
        # This is useful if you accidentally entered something.
        if not self.expenses:
            return None # Nothing to delete
        last = self.expenses.pop()  # Remove last entry
        self._save_expenses() # Save updated list
        self.export_to_csv() # Rebuild CSV so it's up to date
        return last # Return what was deleted

    def get_total(self):
    #Calculate total amount spent across all expenses.
        return round(sum(e['amount'] for e in self.expenses), 2)

    def get_by_category(self):
        #Return a dictionary where each category maps to its total amount.
        #This helps see where our money is going.
        summary = defaultdict(float)
        for e in self.expenses:
            summary[e['category']] += e['amount']
        return dict(sorted(summary.items())) # Sort alphabetically for readability

    def get_trend(self):
        # Group expenses by date and return how much was spent per day.
        # This gives us a timeline view of spending habits.
        trend = defaultdict(float)
        for e in self.expenses:
            trend[e['date']] += e['amount']
        return dict(sorted(trend.items()))

    def get_high_low_categories(self):
        # Determines which category had the most spending and which had the least.
        cat_totals = self.get_by_category()
        if not cat_totals:
            return None, None # No data yet
        high = max(cat_totals.items(), key=lambda x: x[1])
        low = min(cat_totals.items(), key=lambda x: x[1])
        return high, low

    def export_to_csv(self, filename="expenses_report.csv"):
        # This Creates CSV report:
        # Full expense log with running total
        # Totals by category
        # Highest and lowest category
        if not self.expenses: # Nothing to export
            return False

        # Sort by date for neatness and readablity
        expenses_sorted = sorted(self.expenses, key=lambda x: x['date'])
        category_totals = self.get_by_category()
        high, low = self.get_high_low_categories()

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)

            # First section is the expense log
            writer.writerow(["Date", "Category", "Amount", "Running Total"])
            running = 0.0
            for e in expenses_sorted:
                running += e['amount']
                writer.writerow([e['date'], e['category'], f"{e['amount']:.2f}", f"{running:.2f}"])

            # Just a spacer row
            writer.writerow([])
            
             # The second section is the summary by category
            writer.writerow(["Category", "Amount", "", ""])
            for cat, amt in category_totals.items():
                writer.writerow([cat, f"{amt:.2f}", "", ""])

            # another spacer
            writer.writerow([])

            # The third section shows the high and low 
            if high and low:
                writer.writerow(["Highest Spend Category", high[0], f"{high[1]:.2f}", ""])
                writer.writerow(["Lowest Spend Category", low[0], f"{low[1]:.2f}", ""])

        return True  # Tells us that export was successful
