# About the project:
# give how much money I have
# which stock I want to buy.

class MoneyMachine:
    user_budget = 0
    stock_price = 0
    new_user_budget = 0

    def user_portfolio(self):

        self.user_budget = int(raw_input("How much you want to buy :"))  # asking users how much stock they want to buy
        self.stock_price = float(raw_input("Enter stock price :"))  # what is the price of stock

        return self.user_budget, self.stock_price

    def stock_calculation(self):

        number_shares = int(self.user_budget / self.stock_price)  # number of shares a user can buy with the budget
        self.new_user_budget = (
                    number_shares * self.stock_price)  # change the price to round down and claculating a new user budget

        for percent in range(4, 18, 4):  # what is the percentage of profit in diffrent levels

            stock_percentage = (self.stock_price * percent) / 100  # calculate x percent of money
            total_price_after_profit = stock_percentage + self.stock_price
            total_price = ((number_shares * total_price_after_profit) - 20.99) - self.new_user_budget
            print ("{}% <<stop loss at >> {} profit {}").format(percent, total_price_after_profit, total_price)

    # def avrage_down(self): # analizing user's options
    #
    #     # 3000 >> 160 >> 18
    #     # 2000 >> 155 >> 12
    #     number_shares = 0
    #     user_input = "y"
    #     while user_input == "y":
    #         self.user_budget = int (raw_input("How much you want to buy :"))  #3000
    #         self.stock_price = float(raw_input("Enter stock price :")) #160
    #         number_shares = int(self.user_budget / self.stock_price)  #3000/160 = 18
    #         self.new_user_budget = (number_shares * self.stock_price) # 18*160 = 2,880
    #         user_input = raw_input("do you wan to continue: ")
    #
    #     print self.new_user_budget
    #     print number_shares
    #     avrage_down_price = float(self.new_user_budget / number_shares)
    #     print avrage_down_price

    def start_project(self):  # start the project

        while True:
            print ("Press 1 if you want to check the profit")
            print ("Press 2 if you want to check the average down")
            user_input = raw_input("")
            if user_input == "1":
                self.user_portfolio()
                self.stock_calculation()
            elif user_input == "2":
                # self.avrage_down()
                pass


stock = MoneyMachine()
stock.start_project()


