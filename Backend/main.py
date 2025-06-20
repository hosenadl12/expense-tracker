from tracker import ExpenseTracker # We bring in our tracker class from tracker.py


def main():

    # This Creates an instance of our tracker to use
    tracker = ExpenseTracker()

    while True:

        # Display the menu options to the user
        print("\nHOSEN'S EXPENSE TRACKER MENU: ")
        print("1. Add Expense")
        print("2. View Total Expense")
        print("3. View by Category")
        print("4. View Expense Trend")
        print("5. View Highest/Lowest Category")
        print("6. Delete Last Expense")
        print("7. Export to CSV")
        print("8. Exit")

        # Ask for user choice
        choice = input("Select an option (1–8): ").strip()

        # new expense
        if choice == '1':
            cat = input("Category: ").strip().capitalize()
            try:
                amt = float(input("Amount: $"))
                date = input("Date (YYYY-MM-DD) [leave blank for today]: ").strip()
                tracker.add_expense(cat, amt, date if date else None)
                print("✔️ Expense added.")
            except ValueError:
                print("Invalid amount.")



        # Total Spending
        elif choice == '2':
            print(f"Total spent: ${tracker.get_total():.2f}")

        # Breaksdown the spending by category
        elif choice == '3':
            for cat, amt in tracker.get_by_category().items():
                print(f"- {cat}: ${amt:.2f}")


        # How much was spent over time
        elif choice == '4':
            for date, amt in tracker.get_trend().items():
                print(f"- {date}: ${amt:.2f}")

        #Show most and least spent categories
        elif choice == '5':
            high, low = tracker.get_high_low_categories()
            if high and low:
                print(f"Most spent on: {high[0]} (${high[1]:.2f})")
                print(f"Least spent on: {low[0]} (${low[1]:.2f})")
            else:
                print("Not enough data.")
        
        # Removes last recorded expense
        elif choice == '6':
            removed = tracker.delete_last_expense()
            if removed:
                print(f"Removed: {removed}")
            else:
                print("Nothing to delete.")


        # Create a CSV summary of everything
        elif choice == '7':
            if tracker.export_to_csv():
                print("CSV exported successfully.")
            else:
                print("No data to export.")


        # Ends the App 
        elif choice == '8':
            print("Goodbye!")
            break

        # invalid menu selections
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()