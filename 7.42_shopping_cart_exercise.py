print("WELCOME TO JOANINHA'S STORE")
print("***************************")
item = input("What item are you purchasing? ")
price = input(f"What is the price of {item}? ")
qty = input(f"how many {item} are you buying? ")

price = float(price)
qty = int(qty)
total = price * qty

print(f"\nAdded {qty} {item}(s) to shopping cart")
print(f"Subtotal: ${total}")
