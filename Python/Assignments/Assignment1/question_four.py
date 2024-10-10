#  WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed.


# Global variable to store the balance
balance = 0

# Function to deposit money
def deposit_money(amount):
    global balance
    if amount >= 1000:
        balance += amount
        print(f"Deposited {amount}. New balance: {balance}")
    else:
        print("Minimum deposit is 1000.")

# Function to withdraw money
def withdraw_money(amount):
    global balance
    if amount >= 500:
        if amount <= balance:
            balance -= amount
            print(f"Withdrew {amount}. New balance: {balance}")
        else:
            print("Insufficient balance.")
    else:
        print("Minimum withdrawal is 500.")

# Function to check balance
def check_balance():
    global balance
    print(f"Your current balance is: {balance}")

# Menu for the SACCO platform
def sacco_menu():
    while True:
        print("\nWelcome to WITIAcademy Sacco")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Please select an option (1-4): ")

        if choice == '1':
            try:
                amount = int(input("Enter amount to deposit: "))
                deposit_money(amount)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '2':
            try:
                amount = int(input("Enter amount to withdraw: "))
                withdraw_money(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            check_balance()

        elif choice == '4':
            print("Thank you for using WITIAcademy Sacco. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Start the program
sacco_menu()

