text = "Order: pizza, fries, milkshake"
encoded = text.replace("pizza", "1").replace("fries", "2").replace("milkshake", "3")
print(encoded)
# Order: 1, 2, 3

codes = {"pizza": "1", "fries": "2", "milkshake": "3"}
text = "Order: pizza, fries, milkshake"

encoded = text

for value, code in codes.items():
    encoded = encoded.replace(value, code)

print(encoded)
# Order: 1, 2, 3