import os

def create_account(name, initial_balance=0):
    return {
        "name": name,
        "balance": initial_balance,
        "transactions": []
    }

def deposit(account, amount):
    if amount <= 0:
        print("Deposit amount must be positive.")
        return account

    account["balance"] += amount
    account["transactions"].append({"type": "Deposit", "amount": amount})
    record_transaction(account["name"], "Deposit", amount)
    print(f"{account['name']} deposited ${amount}. New balance: ${account['balance']:.2f}.")
    return account

def withdraw(account, amount):
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return account

    if account["balance"] < amount:
        print("Insufficient balance for withdrawal.")
        return account

    account["balance"] -= amount
    account["transactions"].append({"type": "Withdrawal", "amount": amount})
    record_transaction(account["name"], "Withdrawal", amount)
    print(f"{account['name']} withdrew ${amount}. New balance: ${account['balance']:.2f}.")
    return account

def check_balance(account):
    print(f"Current balance for {account['name']}: ${account['balance']:.2f}")
    return account["balance"]

def print_statement(account):
    print(f"\nAccount statement for {account['name']}:\n")
    for transaction in account["transactions"]:
        print(f"- {transaction['type']}: ${transaction['amount']:.2f}")
    print(f"Current balance: ${account['balance']:.2f}\n")

def record_transaction(name, transaction_type, amount):
    filename = f"{name}_transactions.txt"
    with open(filename, "a") as file:
        file.write(f"{transaction_type}: ${amount:.2f}\n")

def main():
    accounts = {}

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Print Statement")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            accounts[name] = create_account(name, initial_balance)
            print(f"Account for {name} created with balance ${initial_balance:.2f}.")

        elif choice == "2":
            name = input("Enter account holder name: ")
            if name in accounts:
                amount = float(input("Enter deposit amount: "))
                accounts[name] = deposit(accounts[name], amount)
            else:
                print("Account not found.")

        elif choice == "3":
            name = input("Enter account holder name: ")
            if name in accounts:
                amount = float(input("Enter withdrawal amount: "))
                accounts[name] = withdraw(accounts[name], amount)
            else:
                print("Account not found.")

        elif choice == "4":
            name = input("Enter account holder name: ")
            if name in accounts:
                check_balance(accounts[name])
            else:
                print("Account not found.")

        elif choice == "5":
            name = input("Enter account holder name: ")
            if name in accounts:
                print_statement(accounts[name])
            else:
                print("Account not found.")

        elif choice == "6":
            print("Exiting the banking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
