text = "Order: 1, 2, 3"
decoded = text.replace("1", "pizza").replace("2", "fries").replace("3", "milkshake")
print(decoded)
# Order: pizza, fries, milkshake

codes = {"pizza": "1", "fries": "2", "milkshake": "3"}
text = "Order: 1, 2, 3"

decoded = text

for value, code in codes.items():
    decoded = decoded.replace(code, value)

print(decoded)
# Order: pizza, fries, milkshake