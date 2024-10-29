# Portfolio Profit Calculator

This project contains a simple implementation of a `Portfolio` class that holds a collection of `Stock` objects. The `Portfolio` class includes methods to calculate the profit between two dates and to obtain the annualized return.

## Features

- Add multiple stocks to a portfolio with specific quantities.
- Calculate the total profit of the portfolio between two given dates.
- Calculate the annualized return of the portfolio between two dates.

## Classes

### Stock

- **Attributes:**

  - `name` (str): The name of the stock.
  - `prices` (dict): A dictionary where the keys are dates (YYYY-MM-DD) and the values are stock prices on those dates.

- **Methods:**
  - `price(date: str) -> float`: Returns the stock price on the given date.

### Portfolio

- **Attributes:**

  - `stocks` (dict): A dictionary holding Stock objects and their respective quantities.

- **Methods:**
  - `add_stock(stock: Stock, quantity: int) -> None`: Adds a stock to the portfolio with the specified quantity.
  - `profit(start_date: str, end_date: str) -> float`: Calculates and returns the profit of the portfolio between two dates.
  - `annualized_return(start_date: str, end_date: str) -> float`: Calculates and returns the annualized return of the portfolio between two dates as a percentage.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```
