# In this question, you are going to write a class that performs basic bank operations like deposit, withdrawal,
# and transfer of money. The class "BankAccount" has two attributs, account_type, and balance.
#
# The bank account should perform the following operations:
# 1. __init__(self, account_type):
#    Description: the constructor creates an account by specifying the account type. The account_type is either 'CHECKING' or 'SAVINGS'. The balance is 0
#       when first creating the account.
#    Input: account_type[String]
# 2. withdraw(self, amount):
#    Description: withdraw amount of money. Only money in the checking account
#       can be withdrawn. Also, there should be a sufficient amount of money available in the
#       account to process a fund withdrawal.
#    Input: amount[float]
#    Return: True if the withdrawal is successful, and False otherwise.
# 3. deposit(self, amount):
#    Description: Deposit amount of money.
#    Input: amount[float]
#    Return: True if the deposit is successful.
# 4. transfer(self, account, amount):
#    Description: Transfer amount of money to another bank account.
#       Only money in checking account can be transferred.
#       Check if the 'account' is a valid bank account. Transfer money to the other account only if
#       the current account has sufficient funds.
#    Input: account[BankAccount], amount[float]
#    Return: True if the transfer is successful and False otherwise.
# 5. display(self):
#    Return: bank account type and balance.
#
# EXAMPLE:
# a = BankAccount('CHECKING')
# b = BankAccount('SAVINGS')
# a.withdraw(100)       -> False
# a.deposit(1000)
# b.deposit(1000)
# a.withdraw(100)       -> True
# b.withdraw(100)       -> False
# a.transfer(b, 100)
# a.display()           -> ('CHECKING', 800)
# b.display()           -> ('SAVINGS', 1100)


class BankAccount:
    ###
    def __init__(self, account_type):
        self.account_type = account_type
        self.balance = 0

    def withdraw(self, amount):
        if self.account_type == 'CHECKING' and self.balance >= amount:
            self.balance = self.balance - amount
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance = self.balance + amount
        return True

    def transfer(self, account, amount):
        if self.account_type == 'CHECKING' and type(account) == BankAccount:
            if self.balance >= amount:
                self.balance = self.balance - amount
                account.balance = account.balance + amount
                return True
            return False
        return False

    def display(self):
        tuple1 = (self.account_type, self.balance)
        return tuple1
    ###