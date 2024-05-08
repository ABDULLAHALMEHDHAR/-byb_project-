menu = ["Espresso", "Americano", "Turkish Coffee", "Spanish Latte", "English tea"]

stock = {
    "Espresso": 10,
    "Americano": 15,
    "Turkish Coffee": 20,
    "Spanish Latte": 25,
    "English tea": 30
}

price = {
    "Espresso": 1.50,
    "Americano": 2.00,
    "Turkish Coffee": 2.50,
    "Spanish Latte": 3.00,
    "English tea": 1.00
}

total_stock_worth = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

print("Total Stock Worth in the Café:", total_stock_worth)

