expenses = []

print("Welcome to Expense Tracker by Aashik")

while True:
    print("\n=====MENU=====")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Spend")
    print("4. Exit")

    try:
        choice = int(input("Please enter your Choice : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        date = input("Enter the date: ")
        category = input("Enter the Category: ")
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid amount. Setting to 0.")
            amount = 0.0
        description = input("Enter the Description: ")

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense is added Successfully")

    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses Added")
        else:
            print("====This is your Expenses====")
            count = 1
            for each in expenses:
                print(f"{count} : {each['date']}, {each['category']} , {each['description']}, {each['amount']}")
                count = count + 1

    elif choice == 3:
        total = 0
        for each in expenses:
            total = total + each["amount"]
        print("\nTotal Spend =", total)

    elif choice == 4:
        print("Thank you for using my System")
        break

    else:
        print("Invalid choice. Try again")