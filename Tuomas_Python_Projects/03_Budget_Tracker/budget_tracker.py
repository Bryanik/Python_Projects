#import json
import json

# Def load_budget_data(filepath)
def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["budget"], data["expenses"]
    except(FileNotFoundError, json.JSONDecodeError):
        return 0, []
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return 0, []

# Def add_expense(expenses, description, amount)
def add_expense(expenses, description, amount):
    expenses.append({"description" : description, "amount" : amount})
    # print "Added expense: Description, Amount: ###"
    print(f"\nAdded expense: {description}, Amount: {amount}")
    return expenses

# Def remove_expense(expenses, description)
def remove_expense(expenses, description):
    deleted_expenses = [expense for expense in expenses if expense["description"] == description]
    expenses = [expense for expense in expenses if expense["description"] != description]
    #print deleted expenses
    [print(f"Deleted: {deleted_expense['description']} - {deleted_expense['amount']}") for deleted_expense in deleted_expenses]
    
    return expenses

# Def get_total_expenses(expenses)
def get_total_expenses(expenses):
    total_expense = sum(expense['amount'] for expense in expenses)
    return total_expense
# Def get_balance(budget, expenses)
def get_balance(budget, expenses):
    total_expense = sum(expense['amount'] for expense in expenses)
    balance = budget - total_expense
    return balance

# Def show_budget_details(budget, expenses)
def show_budget_details(budget, expenses):
    # print "Total budget: ###"
    print(f"\nTotal budget: {budget}")
    # print "Expenses: "
    print("\nExpenses: ")
    # for each expense print "- Description: amount"
    [print(f"- {expense['description']}: {expense['amount']}") for expense in expenses]
    # print "Total Spent: {Execute get_total_expenses(expenses)}"
    print(f"Total spent: {get_total_expenses(expenses)}")
    # print "Remaining Budget: {Execute {get_balance(budget, expenses)}}"
    print(f"Remaining budget: {get_balance(budget, expenses)}")

# Def save_budget_data(filepath, budget, expenses)
def save_budget_data(filepath, budget, expenses):
    data = {"budget": budget, "expenses": expenses}

    with open(filepath, 'w') as file:
        json.dump(data, file)
        print("\nBudget file saved.")

# Def main fxn
def main():
    # Print "Welcome to the Budget App"
    print("Welcome to the Budget App")
    # Define filepath for data storage as "budget_data.json"
    filepath = "budget_data.json"
    # Retrieve initial budget and expenses by calling load_budget_data(filepath)
    budget, expenses = load_budget_data(filepath)
    # If budget equals zero, user should input budget, "Please enter your budget: "
    if (budget == 0):
        budget = float(input("Please enter your budget: "))
        # Expenses should already be returned as an empty list [] from load_budget_data(filepath) if not found

    # Using an infinite loop print
    while True:
        # "What would you like to do?"
        print("\nWhat would you like to do? ")
        # "1. Add an expense"
        print("1. Add an expense")
        # "2. Remove an expense"
        print("2. Remove an expense")
        # "3. Show budget details"
        print("3. Show budget details")
        # "4. Update budget"
        print("4. Update budget")
        # "5. Exit"
        print("5. Exit application")
        # Receive user input "Enter your choice (1/2/3/4/5): "
        choice = int(input("Enter your choice from 1 to 5: "))

        # if 1
        if choice == 1:
            # Input description "Enter expense description: "
            description = input("\nEnter expense description: ")
            # Input amount and convert to float, "Enter expense amount: "
            amount = float(input("\nEnter expense amount: "))
            # execute add_expense(expenses, description, amount)
            expenses = add_expense(expenses, description, amount)

        # if 2
        elif choice == 2:
            # Input description to be removed
            description = input("\nEnter expense description to remove.\nKindly note that all expenses with this description will be removed!: ")
            # execute remove_expense(expenses, description)
            expenses = remove_expense(expenses, description)

        # if 3
        elif choice == 3:
            # Execute show_budget_details(budget, expenses)
            show_budget_details(budget, expenses)

        # if 4
        elif choice == 4:
            budget = float(input("Please enter your new budget: "))
            print(f"\nBudget updated to {budget}")

        # if 5
        elif choice == 5:
            # execute save_budget_data(filepath, initial_budget, expenses)
            save_budget_data(filepath, budget, expenses)
            # print "Exiting Budget App. Goodbye!"
            print("Exiting Budget App. Goodbye!")
            # Break out of infinite loop
            break

        # if input is invalid print "Invalid choice, please choose again."
        else: 
            print("Invalid choice, please try again.")

# Execute main only if the main function
if __name__ == "__main__":
    main()