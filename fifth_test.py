class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner} \nBalance info: {self.balance} eur'

    def deposit(self, deposit):
        self.balance += deposit
        print('Deposit approved, new balance is: ' + str(self.balance) + ' eur')

    def withdraw(self, withdraw):
        self.balance -= withdraw

        if self.balance > 0:
            print('Withdraw approved, new balance is: ' + str(self.balance) + ' eur')
        else:
            print('Insufficient funds')


acct1 = Account('Sergei', 100)

acct1.deposit(50)
acct1.withdraw(150)