class Account:
    def __init__(self, amount):
        self._amount = amount

    def transfer(self, amount, dest_account):
        dest_account._amount = dest_account._amount + amount
        self._amount = self._amount - amount

    def amount(self):
        return self._amount
