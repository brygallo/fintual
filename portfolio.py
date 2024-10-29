from datetime import datetime

class Stock:
    def __init__(self, name, prices):
        """
        Initializes the Stock object with a name and a dictionary of prices.
        :param name: The name of the stock.
        :param prices: A dictionary where keys are dates (YYYY-MM-DD) and values are the stock prices.
        """
        self.name = name
        self.prices = prices

    def price(self, date):
        """
        Returns the stock price on the given date.
        :param date: A string representing a date (YYYY-MM-DD).
        :return: The stock price on the given date.
        """
        return self.prices.get(date, 0)


class Portfolio:
    def __init__(self):
        """
        Initializes an empty portfolio with a collection of stocks.
        """
        self.stocks = {}

    def add_stock(self, stock, quantity):
        """
        Adds a stock to the portfolio.
        :param stock: A Stock object.
        :param quantity: Number of shares of the stock.
        """
        self.stocks[stock] = quantity

    def profit(self, start_date, end_date):
        """
        Calculates the total profit of the portfolio between two dates.
        :param start_date: A string representing the start date (YYYY-MM-DD).
        :param end_date: A string representing the end date (YYYY-MM-DD).
        :return: The total profit of the portfolio between the two dates.
        """
        total_profit = 0
        for stock, quantity in self.stocks.items():
            start_price = stock.price(start_date)
            end_price = stock.price(end_date)
            total_profit += (end_price - start_price) * quantity
        return total_profit

    def annualized_return(self, start_date, end_date):
        """
        Calculates the annualized return of the portfolio between two dates.
        :param start_date: A string representing the start date (YYYY-MM-DD).
        :param end_date: A string representing the end date (YYYY-MM-DD).
        :return: The annualized return of the portfolio as a percentage.
        """
        total_profit = self.profit(start_date, end_date)
        initial_value = sum(stock.price(start_date) * quantity for stock, quantity in self.stocks.items())
        
        if initial_value == 0:
            return 0

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days_between = (end - start).days
        years_between = days_between / 365.25

        if years_between == 0:
            return 0

        total_return = total_profit / initial_value
        annualized_return = ((1 + total_return) ** (1 / years_between)) - 1
        return annualized_return * 100


# Example usage:
# Define stock prices over time
stock_a_prices = {
    "2024-01-01": 100,
    "2024-06-01": 150,
    "2024-12-01": 200
}

stock_b_prices = {
    "2024-01-01": 50,
    "2024-06-01": 75,
    "2024-12-01": 80
}

# Create Stock objects
stock_a = Stock("Stock A", stock_a_prices)
stock_b = Stock("Stock B", stock_b_prices)

# Create a Portfolio and add stocks
portfolio = Portfolio()
portfolio.add_stock(stock_a, 10)
portfolio.add_stock(stock_b, 20)

# Calculate profit and annualized return
profit = portfolio.profit("2024-01-01", "2024-12-01")
annualized_return = portfolio.annualized_return("2024-01-01", "2024-12-01")

print(f"Profit: ${profit}")
print(f"Annualized Return: {annualized_return:.2f}%")
