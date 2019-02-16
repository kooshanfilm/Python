
# About the project:
# give how much money I have
# which stock I want to buy

class MoneyMachine():

    def user_portfolio(self):
        global user_budget
        global stock_price
        user_budget = int (raw_input("How much you want to buy :"))
        stock_price = float(raw_input("Enter stock price :"))

        return user_budget ,stock_price

    def stock_calculation(self):

        number_shares = int (user_budget / stock_price)
        new_user_budget = number_shares * stock_price

        for percent in range(3,18,3):
            stock_percentage = (stock_price * percent ) /100  # calculate five percent of money
            total_price_after_profit = stock_percentage + stock_price
            total_price = ((number_shares * total_price_after_profit) - 20.99) - new_user_budget
            print ("{}% <<stop loss at >> {} profit {}").format(percent,total_price_after_profit ,total_price)


    def start_cal(self):
        user_input = "y"
        while user_input == "y":
            self.user_portfolio()
            self.stock_calculation()
            user_input = raw_input("Continue < y > < n >")
def main():

    stock = MoneyMachine()
    stock.start_cal()
if __name__ == '__main__':
    main()