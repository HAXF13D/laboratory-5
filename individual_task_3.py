"""Variant 3"""

current_day = float(10)
percent = 1.1
summa = 0

for i in range(7):
    summa += current_day
    current_day *= percent

print("Ran in 7 days: %.3f" % summa)
