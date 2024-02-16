from expense import Expense

def main():
    print(f"Running Expense Tracker!")


    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file
    save_expense_to_file(expense)


    # Read file and summarize expenses
    summarize_expenses()
    
    
def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    #print(f"You've entered {expense_name},{expense_name}")

    expense_categories = [
        "Food", 
        "Home",
        "Work", 
        "fun",
        "Misc",
        "Save",
        "id",
        "title",
        "subtitle",
        "authors",
        "publisher",
        "published_date",
        "category",
        "distribution_expense",
    ]
    
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) -1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name = expense_name, category = selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Pick out off the list.")
        
        
def save_expense_to_file(expense):
    print(f"Saving User Expense: {expense}")


def summarize_expenses():
    print(f"Summarizing  User Expense")
    


if __name__=="__main__":
    main()