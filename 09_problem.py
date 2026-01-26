'''Expense Tracker (Moderate)
What to build
Add daily expenses
Category wise total
Show total spending
Concepts used
Dictionary for category → amount
Loop for adding expenses
Functions for calculations
Strings for categories
if-else for validation'''
expenses={"food":0,
      "travel":0,
      "study":0}
def thing():
    category=input("Enter the category:")
    amt=int(input("Enter the amount:"))
    if category in expenses:
        expenses[category] = expenses[category] + amt
    else:
        print("Invalid category")
def show_total():
    total = 0
    for amount in expenses.values():
        total += amount
    print("Total spending:", total)
def category_total():
    category = input("Enter category: ").lower()
    if category in expenses:
        print(f"You spent {expenses[category]} on {category}")
    else:
        print("Invalid category")

while True:
    print("\n1. Add expense")
    print("2. Show total spending")
    print("3. Category wise total")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        thing()
    elif choice == 2:
        show_total()
    elif choice == 3:
        category_total()
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
