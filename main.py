import time  # For implementing idle timeout
import random  # For randomized fun messages
from datetime import datetime  # For recording transaction timestamps

# Muhammed's Banking System (MBS)

# Custom fun messages for being broke
broke_messages = [
    "Oops! Looks like you're running low. Sort it out lad!",
    "You're broke. I'm disappointed!",
    "Insufficient funds. How does it feel to be broke?"
]

# Fun messages for successful withdrawals
withdraw_success_messages = [
    "Enjoy your cash responsibly!",
    "Money well withdrawn. Spend wisely!",
    "Here's your hard-earned money!"
]

# Fun messages for successful deposits
deposit_success_messages = [
    "Your money is in safe hands!",
    "Great job saving for the future!",
    "Deposit successful. Keep up the good work!"
]

# Set up multiple accounts
accounts = {
    "Savings": 1000.0,  # Starting balance for Savings account
    "Current": 500.0    # Starting balance for Current account
}

transaction_history = []  # List to store transaction records

print("Welcome to Muhammed's Banking System (MBS)\n\nPlease insert your bank card")

# PIN Authentication setup
password = 1997  # Predefined PIN for the customer
attempts = 3  # Maximum number of attempts allowed for entering the correct PIN

# Authenticate the user's PIN
while attempts > 0:
    try:
        # Prompt the user for their PIN
        pin = int(input("Please enter your PIN code: "))
        
        if pin == password:
            print("Your PIN is correct. Authentication complete.")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. You have {attempts} attempts left.")
    except ValueError:
        print("Invalid input. Please enter a numeric PIN.")

# If all attempts are used, block access
if attempts == 0:
    print("You have failed the authentication process. Please contact customer service.")
else:
    # Allow user to select an account type
    print("\nAvailable Accounts:")
    for account in accounts:
        print(f"- {account}")
    
    selected_account = input("Choose an account (Savings/Current): ").capitalize()
    if selected_account in accounts:
        print(f"You are now using the {selected_account} account.")
        balance = accounts[selected_account]  # Use the selected account's balance
    else:
        print("Invalid account selection. Defaulting to Savings.")
        selected_account = "Savings"
        balance = accounts[selected_account]

    # Start the session timer
    IDLE_TIMEOUT = 30  # Set idle timeout in seconds
    last_activity = time.time()  # Record the last activity time

    while True:
        # Check for idle timeout
        if time.time() - last_activity > IDLE_TIMEOUT:
            print("Session timed out due to inactivity. Please log in again.")
            break

        # Display the main menu
        print("\n--- Main Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")
        
        try:
            # Prompt the user to choose an option
            choice = int(input("Enter your choice (1-5): "))
            last_activity = time.time()  # Reset the activity timer

            if choice == 1:
                print(f"Your current balance is: £{balance:.2f}")
            elif choice == 2:
                deposit = float(input("Enter the amount to deposit: £"))
                if deposit > 0:
                    balance += deposit
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    transaction_history.append(f"[{timestamp}] Deposited: £{deposit:.2f}")
                    print(random.choice(deposit_success_messages))
                else:
                    print("You need to deposit a positive amount.")
            elif choice == 3:
                withdraw = float(input("Enter the amount to withdraw: £"))
                if 0 < withdraw <= balance:
                    balance -= withdraw
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    transaction_history.append(f"[{timestamp}] Withdrew: £{withdraw:.2f}")
                    print(random.choice(withdraw_success_messages))
                elif withdraw > balance:
                    print(random.choice(broke_messages))
                else:
                    print("Withdrawal amount must be positive.")
            elif choice == 4:
                if transaction_history:
                    print("\n--- Transaction History ---")
                    for transaction in transaction_history:
                        print(transaction)
                else:
                    print("No transactions recorded.")
            elif choice == 5:
                print(f"Goodbye! Thank you for using the {selected_account} account in MBS.")
                accounts[selected_account] = balance  # Save the updated balance
                break
            else:
                print("Invalid choice. Please select an option between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
