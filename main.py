class Stock:
    def __init__(self, symbol, name, price, quantity):
        self.symbol = symbol
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        self.price = new_price

    def get_value(self):
        return self.price * self.quantity

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.stocks.remove(stock)
                print(f"Stock {symbol} removed from portfolio.")
                return
        print(f"Stock {symbol} not found in portfolio.")

    def get_portfolio_value(self):
        total_value = 0
        for stock in self.stocks:
            total_value += stock.get_value()
        return total_value

    def display_portfolio(self):
        if not self.stocks:
            print("Portfolio is empty.")
        else:
            print("Portfolio:")
            for stock in self.stocks:
                print(f"{stock.symbol}: {stock.name}, Quantity: {stock.quantity}, Current Price: ${stock.price}, Total Value: ${stock.get_value()}")

def main():
    portfolio = Portfolio()

    # Add some sample stocks
    portfolio.add_stock(Stock("AAPL", "Apple Inc.", 150.25, 10))
    portfolio.add_stock(Stock("GOOGL", "Alphabet Inc.", 2800.75, 5))
    portfolio.add_stock(Stock("MSFT", "Microsoft Corporation", 300.50, 8))

    while True:
        print("\nMenu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Get Portfolio Value")
        print("4. Display Portfolio")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            name = input("Enter stock name: ")
            price = float(input("Enter stock price: "))
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(Stock(symbol, name, price, quantity))
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ")
            portfolio.remove_stock(symbol)
        elif choice == "3":
            print(f"Portfolio Value: ₹{portfolio.get_portfolio_value()}")
        elif choice == "4":
            portfolio.display_portfolio()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
