print("Welcome to BLS Expense Tracker App.")
print("Please enter your details to track your expenses.")
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

print(f"\n{first_name} {last_name}, let's start tracking your expenses.")
total_income = input("Please enter your total monthly income: ")
print("Note: Your expense limit is 60% of your total monthly income. Now please enter your expenses for the month below.")

expense1 = input("\nPlease enter your expense for food: ")
expense2 = input("Please enter your expense for transportation: ")
expense3 = input("Please enter your expense for data: ")
expense4 = input("Please enter your expense for miscellaneous: ")

if total_income.isdigit() and expense1.isdigit() and expense2.isdigit() and expense3.isdigit() and expense4.isdigit():
   
    total_income = int(total_income)
    expense1 = int(expense1)
    expense2 = int(expense2)
    expense3 = int(expense3)
    expense4 = int(expense4)

    if total_income == 0:
        print("Your total income cannot be zero. Please enter a valid income and try again.")
    else:               
        expense_limit = round((60/100) * total_income)

                
        total_expenses = expense1 + expense2 + expense3 + expense4
                    
        if total_expenses > expense_limit:
            print(f"Your total expenses of {total_expenses} exceed your limit of {expense_limit} for the month. please cut down on your expenses next month.")
        else:
            print(f"Your total expense which is {total_expenses} is within your limit of {expense_limit}. Good job,We go again next month")
            
else:
    print("Please enter amount in numeric form only. review expenses and limit and try again.")

