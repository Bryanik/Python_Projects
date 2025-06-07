# Budget App

Welcome to the Budget App! This application helps you manage your budget by tracking your expenses, allowing you to add and remove expenses, view budget details, and update your budget.

## Features

- Load budget data from a JSON file.
- Add and remove expenses.
- Show budget details including total budget, expenses, total spent, and remaining budget.
- Update the budget.
- Save budget data to a JSON file.

## Functions

### `load_budget_data(filepath)`

Loads budget data from a specified JSON file.

- **Parameters**: 
  - `filepath` (str): The path to the JSON file.
- **Returns**: 
  - `budget` (float): The total budget.
  - `expenses` (list): The list of expenses.
- **Exceptions**: 
  - Returns a budget of 0 and an empty list if the file is not found or is invalid JSON.

### `add_expense(expenses, description, amount)`

Adds an expense to the list of expenses.

- **Parameters**: 
  - `expenses` (list): The list of expenses.
  - `description` (str): A description of the expense.
  - `amount` (float): The amount of the expense.
- **Returns**: 
  - Updated list of expenses.

### `remove_expense(expenses, description)`

Removes all expenses with the given description from the list of expenses.

- **Parameters**: 
  - `expenses` (list): The list of expenses.
  - `description` (str): The description of the expense to be removed.
- **Returns**: 
  - Updated list of expenses.

### `get_total_expenses(expenses)`

Calculates the total of all expenses.

- **Parameters**: 
  - `expenses` (list): The list of expenses.
- **Returns**: 
  - Total amount of expenses (float).

### `get_balance(budget, expenses)`

Calculates the remaining budget after accounting for expenses.

- **Parameters**: 
  - `budget` (float): The total budget.
  - `expenses` (list): The list of expenses.
- **Returns**: 
  - Remaining budget (float).

### `show_budget_details(budget, expenses)`

Displays the budget details, including total budget, list of expenses, total spent, and remaining budget.

- **Parameters**: 
  - `budget` (float): The total budget.
  - `expenses` (list): The list of expenses.

### `save_budget_data(filepath, budget, expenses)`

Saves the budget data to a specified JSON file.

- **Parameters**: 
  - `filepath` (str): The path to the JSON file.
  - `budget` (float): The total budget.
  - `expenses` (list): The list of expenses.

## Main Function

### `main()`

The main function that drives the Budget App. It provides a user interface for interacting with the budget data.

- Loads budget data from a JSON file.
- Prompts the user to enter a budget if none exists.
- Provides options to add or remove expenses, show budget details, update the budget, or exit the application.
- Saves the budget data to a JSON file upon exiting.

## How to Run

1. Ensure you have Python installed.
2. Save the code in a file named `budget_app.py`.
3. Run the script using the command:
   ```bash
   python budget_app.py
   ```

Follow the on-screen prompts to manage your budget!

## Example Usage

```bash
Welcome to the Budget App

Please enter your budget: 1000

What would you like to do?
1. Add an expense
2. Remove an expense
3. Show budget details
4. Update budget
5. Exit application

Enter your choice from 1 to 5: 1
Enter expense description: Groceries
Enter expense amount: 100

Added expense: Groceries, Amount: 100

What would you like to do?
1. Add an expense
2. Remove an expense
3. Show budget details
4. Update budget
5. Exit application

Enter your choice from 1 to 5: 3

Total budget: 1000

Expenses:
- Groceries: 100

Total spent: 100
Remaining budget: 900

...

Exiting Budget App. Goodbye!
```