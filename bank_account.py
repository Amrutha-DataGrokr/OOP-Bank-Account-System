
class BankAccount:
    def __init__(self,account_number:str,holder_name:str,balance:float)->None:
        self.account_number=account_number
        self.holder_name=holder_name
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self._balance=balance
        self.transaction_history=[]

    def _record_transaction(self, transaction_type:str, amount:float)->None:
        history = {
            "type": transaction_type,
            "amount": amount,
            "balance_after": self._balance
        }
        self.transaction_history.append(history)

    def deposit(self,amount:float)->None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance+=amount
        self._record_transaction("Deposit",amount)
        print(f"Amount:{amount} deposited successfully!")
        print(f"Current Balance:{self._balance}")
        
    def withdraw(self,amount:float)->None:
        if amount<=0:
            raise ValueError("Withdrawal amount must be positive.")
        if self._balance<amount:
            raise ValueError("Insufficient Balance.")
        self._balance-=amount
        self._record_transaction("Withdrawal",amount)
        print(f"Amount:{amount} withdrawn successfully!\nCurrent Balance:{self._balance}")
        
    def get_balance(self)->float:
        return self._balance

class SavingsAccount(BankAccount):
    def __init__(self,account_number:str,holder_name:str,balance:float,interest_rate:float)->None:
        super().__init__(account_number,holder_name,balance)
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.interest_rate=interest_rate

    def apply_interest(self)->None:
        interest=self._balance*(self.interest_rate/100)
        self._balance+=interest
        self._record_transaction("Interest",interest)
        print(f"Interest Earned:{interest}")
        print(f"Current Balance:{self._balance}")

class CurrentAccount(BankAccount):
    def __init__(self,account_number:str,holder_name:str,balance:float,overdraft_limit:float)->None:
        super().__init__(account_number,holder_name,balance)
        if overdraft_limit<0:
            raise ValueError("Overdraft limit cannot be negative.")
        self.overdraft_limit=overdraft_limit

    def withdraw(self, amount:float)->None:
        max_withdraw=self._balance+self.overdraft_limit
        if amount<=0:
            raise ValueError("Withdrawal amount must be positive.")
        if  amount>max_withdraw:
            raise ValueError("Insufficient Balance.")
        self._balance-=amount
        self._record_transaction("Withdrawal", amount)
        print(f"Amount: {amount} withdrawn successfully!")
        print(f"Current Balance: {self._balance}")
    
