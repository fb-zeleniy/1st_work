from array import *
import math

products_prices = [200, 100, 24, 1500, 1500]
min_price = min(products_prices)
max_price = max(products_prices)
middle_price = sum(products_prices) / len(products_prices)

print(f"Максимальная цена: {min_price}")
print(f"Минимаьлная цена: {max_price}")
print(f"Средняя цена: {middle_price}")