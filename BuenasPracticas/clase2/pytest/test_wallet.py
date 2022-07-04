import pytest
from wallet import Wallet,InsuficienteSaldo
# pytest test_wallet.py 
def test_cantidad_inicial():
    wallet_ruben=Wallet()
    assert wallet_ruben.balance==0

def test_set_cantidad_inicial():
    wallet1=Wallet(100)
    assert wallet1.balance==100

def test_spend():
    wallet1=Wallet(100)
    wallet1.spend_cash(10)
    assert wallet1.balance==90

def test_add():
    wallet1=Wallet(100)
    wallet1.add_cash(10)
    assert wallet1.balance==110

def test_spend():
    wallet1=Wallet()
    with pytest.raises(InsuficienteSaldo):
        wallet1.spend_cash(101)
    