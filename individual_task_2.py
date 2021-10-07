"""Variant 2"""

x = int(input("x: "))
y = int(input("y: "))

if x * x * y > x * y * y:
    ma = x * x * y
else:
    ma = x * y * y

if x - y < x + 2 * y:
    mi = x - y
else:
    mi = x + 2 * y

u = ma ** 2 + mi ** 2
print(u)
