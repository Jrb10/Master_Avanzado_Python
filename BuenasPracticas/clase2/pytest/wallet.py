class InsuficienteSaldo(Exception):
    pass


class Wallet():
    def __init__(self,amount=0) -> None:
        self.balance=amount

    def spend_cash(self,amount):
        if self.balance<amount:
            raise InsuficienteSaldo("No hay suficiente saldo")
        self.balance-=amount

    def add_cash(self,amount):
        self.balance+=amount