"""Variant 12"""

x1 = int(input("Price per roll of wallpaper: "))
x2 = int(input("Price for a can of paint: "))

price = float(8 * x1 + 2 * x2)

if 200 <= price <= 500:
    price = price * 0.97
elif 500 < price <= 800:
    price = price * 0.95
elif 800 < price <= 1000:
    price = price * 0.93
elif price > 1000:
    price = price * 0.91

print("Total price = %.2f" % price)
