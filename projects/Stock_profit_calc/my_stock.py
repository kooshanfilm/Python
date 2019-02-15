

# About the project:
# give how much money I have
# which stock I want to buy

class MoneyMachine():


    def user_portfolio(self):
        global user_budget
        global stock_price
        user_budget = int (raw_input("Enter amount :"))
        # stock_sym = raw_input("Stock sym or manual enter")
        stock_price = float(raw_input("Enter stock price :"))

        return user_budget,stock_price

    def stock_calculation(self):

        number_shares = int (user_budget / stock_price)

        five_percent = (MoneyMachine.stock_price * 5)/100 # calculate five percent of money
        print number_shares

        # print ("Number of shares you can buy:{} ".format(number_shares))







def main():

    stock = MoneyMachine()
    stock.user_portfolio()
    stock.stock_calculation()


if __name__ == '__main__':
    main()