# Expense Tracker

Hi! I'm Hosen Sadeghiadl, and this is a command line app I built to help track everyday expenses without needing a database or any fancy setup. Just run it, add your expenses, and get summaries and reports that are all saved to a file.

-- 

## What You Can Do

- Add an expense with a category, amount, and optional date
- See your total spending
- Get a breakdown of spending by category
- Track how your spending changes over time
- Find out where you’re spending the most and the least
- Delete your last expense if you made a mistake
- Export everything to a CSV report

---

## Project Structure

- Expense_Tracker/
  - backend/
    - main.py – handles the menu and user input
    - tracker.py – contains all logic for managing expenses
  - Data/
    - expenses.json – stores all expense records
  - README.md – you're reading this!


---

## How to Run It! 
Make sure Python 3 is installed on your computer!

Then:

cd backend
python3 main.py

-- 

## CSV Report
When you choose option 7 from the menu, the app creates a file called expenses_report.csv.
This report includes:
- A list of all your expenses (sorted by date)
- A running total
- Spending by category
- Highest and lowest spending categories
- Perfect for budgeting or just keeping track of where your money goes.


## How It Works Behind the Scenes
- Everything is stored in a .json file which helps not require a database
- CSV reports are built with Python’s built-in csv module
- Data is organized by category and date, and sorted so it's easy to read
- You don’t need to install any extra libraries! 

