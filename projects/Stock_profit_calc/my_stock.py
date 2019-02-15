
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

        return user_budget ,stock_price

    def stock_calculation(self):

        number_shares = int (user_budget / stock_price)
        new_user_budget = number_shares * stock_price
        five_percent = (stock_price * 5 ) /100  # calculate five percent of money
        stock_five_percent = five_percent + stock_price
        five_percent_profite = ((number_shares * stock_five_percent) - 20.99) - new_user_budget

        print ("5% profit sell at {} to make {}").format(stock_five_percent ,five_percent_profite)

def main():

    stock = MoneyMachine()
    stock.user_portfolio()
    stock.stock_calculation()


if __name__ == '__main__':
    main()