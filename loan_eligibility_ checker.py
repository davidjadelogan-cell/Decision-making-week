print("Welcome to BLS Loaning App")
print("Please enter your details to check your loan eligibility.")
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
age = input("Please enter your age: ")
employment_status = input("Please enter your employment status (Yes/No): ").lower()
income = input("Please enter your monthly income: ")

if age.isdigit() and income.isdigit() and employment_status in ["yes", "no"]:
    age = int(age)
    income = int(income)
    if age < 18:
        print(f"Sorry {first_name} {last_name}, you are must be 18+ to be eligible for a loan.")
    elif employment_status == "no":
        print(f"Sorry {first_name} {last_name}, you must be employed to be eligible for a loan.")

    elif income < 200000:
        print(f"Sorry {first_name} {last_name}, you must have a monthly income of at least 200,000 to be eligible for a loan.")
    else:
        print(f"Congratulations {first_name} {last_name}, you are eligible for a loan.")
else:
    print("Invalid input. Please check your income and age details (must be numbers) and employment status (Yes/No).")