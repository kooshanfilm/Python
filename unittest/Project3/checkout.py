


class Checkout:

    def __init__(self):
        self.prices = {}
        self.total = 0


    def addItemPrice(self,item,price):
        if item not in self.prices:
            raise Exception("bad item")
        self.prices[item]  = price

    #testing this function:
        # def test_itemprice(checkout):
        #     checkout.itemprice("test",12)



    def addItem(self,item):
        self.total += self.prices(item)

    def totlacheckout(self):
        return self.total

