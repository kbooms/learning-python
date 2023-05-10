
item = input("What are ya buyin? ")
price = float(input("What are ya payin? "))
quantity = int(input("How many ya want? "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")