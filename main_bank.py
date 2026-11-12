
from bank_account import BankAccount, SavingsAccount, CurrentAccount


def display_transaction_history(account: BankAccount) -> None:
    print(f"\nTransaction History: {account.account_number}")
    print(f"Account Holder: {account.holder_name}")

    for transaction in account.transaction_history:
        print(transaction)

def main() -> None:
    # Creating 2 Savings Accounts and 1 Current Account
    accounts = [
        SavingsAccount("S101", "Alice", 10000, 5),
        SavingsAccount("S102", "Bob", 15000, 4),
        CurrentAccount("C101", "Charlie", 5000, 2000)
    ]

    # Deposits
    print("\n========== DEPOSITS ==========")
    accounts[0].deposit(2000)
    accounts[1].deposit(3000)
    accounts[2].deposit(1000)

    # Withdrawals - Demonstrating Polymorphism
    print("\n========== WITHDRAWALS ==========")

    for account in accounts:
        account.withdraw(2000)

    # Applying Interest to Savings Accounts
    print("\n========== APPLYING INTEREST ==========")

    for account in accounts:
        if isinstance(account, SavingsAccount):
            account.apply_interest()

    # Displaying Transaction Histories
    print("\n========== TRANSACTION HISTORIES ==========")

    for account in accounts:
        display_transaction_history(account)


if __name__ == "__main__":
    main()
