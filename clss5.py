class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Wallet:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount

    def add_money(self, income):
        if income > 0:
            self.amount += income
            return f"Added ${income}. Total amount: ${self.amount}"
        else:
            return "Invalid income amount."

    def spend_money(self, expense):
        if expense > 0 and expense <= self.amount:
            self.amount -= expense
            return f"Spent ${expense}. Total amount: ${self.amount}"
        elif expense <= 0:
            return "Invalid expense amount."
        else:
            return "Insufficient funds."

person_name = input("Enter the person's name: ")
person_age = int(input("Enter the person's age: "))
person = Person(person_name, person_age)

while True:
    print("\nOptions:")
    print("1. Add Money")
    print("2. Spend Money")
    print("3. Check Wallet Balance")
    print("4. Exit")
    choice = input("Select an option (1/2/3/4): ")

    if choice == '1':
        income = int(input("Enter the income amount: "))
        print(person.name, "now", person.name, "has", person.age, "years old.")
    elif choice == '2':
        expense = int(input("Enter the expense amount: "))
        print(person.name, "now", person.name, "has", person.age, "years old.")
    elif choice == '3':
        print(f"Wallet balance for {person.name}: ${person.age}")
    elif choice == '4':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option.")
