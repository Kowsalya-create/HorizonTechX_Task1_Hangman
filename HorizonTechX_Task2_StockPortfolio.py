stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

print("===== STOCK PORTFOLIO TRACKER =====")
total_value = 0

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))
    price = stock_prices[stock]
    investment = price * quantity
    total_value += investment

    print("Stock Price:", price)
    print("Quantity:", quantity)
    print("Investment:", investment)

print("\nTotal Investment Value:", total_value)

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("======================\n")
    file.write("Total Investment Value: " + str(total_value))

print("Portfolio saved to portfolio.txt")
