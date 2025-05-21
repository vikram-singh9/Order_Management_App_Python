# Restaurant Menu Dictionary
menu = {
    "Paneer Tikka": 180,
    "Chicken Wings": 220,
    "Spring Rolls": 160,
    "French Fries": 120,
    "Butter Chicken": 320,
    "Paneer Butter Masala": 280,
    "Veg Biryani": 200,
    "Chicken Biryani": 250,
    "Tandoori Roti": 20,
    "Butter Naan": 30,
}

print("🍽️ Welcome to Vikram's Restaurant!")
print("Here's our menu")
for i, meal in enumerate(menu.keys(), start=1):
    print(f"{i}. {meal}")
# Show menu to user
print("🍽️ Welcome to Vikram's Restaurant!")
print("Here's our individual menu food prices\n")
for item, price in menu.items():
    print(f"{item} - ₹{price}")

print("\n📝 Let's take your order (type 'done' to finish):\n")

# Take order from user
order = {}
while True:
    item = input("Enter item name(If entered all type \"done\"): ").strip()
    if item.lower() == 'done':
        break
    elif item in menu:
        try:
            quantity = int(input(f"Enter quantity for {item}: "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        except ValueError:
            print("❌ Please enter a valid number.")
    else:
        print("❌ Item not found in menu.")

# Calculate total bill
print("\n🧾 Your Bill Summary:\n")
total = 0
for item, quantity in order.items():
    price = menu[item]
    cost = price * quantity
    total += cost
    print(f"{item} x {quantity} = ₹{cost}")

print(f"\n💰 Total Amount to Pay: ₹{total}")
print("\n🙏 Thank you for dining with us, you're welcome again!")

