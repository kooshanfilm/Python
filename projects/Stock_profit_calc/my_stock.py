
# About the project:
# give how much money I have
# which stock I want to buy.

class MoneyMachine:
    user_budget = 0
    stock_price = 0
    new_user_budget = 0
    def user_portfolio(self):

        self.user_budget = int (raw_input("How much you want to buy :"))
        self.stock_price = float(raw_input("Enter stock price :"))

        return self.user_budget ,self.stock_price

    def stock_calculation(self):
        number_shares = int (self.user_budget / self.stock_price)
        self.new_user_budget = number_shares * self.stock_price

        for percent in range(4,18,4):
            stock_percentage = (self.stock_price * percent ) /100  # calculate x percent of money
            total_price_after_profit = stock_percentage + self.stock_price
            total_price = ((number_shares * total_price_after_profit) - 20.99) - self.new_user_budget
            print ("{}% <<stop loss at >> {} profit {}").format(percent,total_price_after_profit ,total_price)


    def stock_analize(self):

        print self.new_user_budget


    # start the project
    def start_project(self):
        user_input = "y"
        while user_input == "y":
            self.user_portfolio()
            self.stock_calculation()
            self.stock_analize()
            user_input = raw_input("Continue < y > < n >")



def main():

    stock = MoneyMachine()
    stock.start_project()
    stock.stock_analize()
if __name__ == '__main__':
    main()




