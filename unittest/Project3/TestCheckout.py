import pytest
from .checkout import Checkout


@pytest.fixture()
def checkout():
    a = Checkout()
    return a

# def test_CanAddItemPrice(checkout):
#
#     checkout.addItemPrice("a",1)
#
#
# def test_CanItem(checkout):
#
#     checkout.addItem("a")

def test_CanCalcutatorTotal(checkout):
    checkout.addItemPrice("a",1)
    checkout.addItem("a")
    assert checkout.totlacheckout() == 1


def test_Getcorrecttottalmultipleitems(checkout):
    checkout.addItemPrice("a",1)
    checkout.addItemPrice("a",2)
    checkout.addItem("a")




def test_Exceptionwithbaditem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")
