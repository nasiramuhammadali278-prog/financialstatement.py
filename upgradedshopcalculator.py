greetings = ("Greeting our customers")

print(greetings)

items = {
    "Bread": 1300,
    "Cupcakes": 1200,
    "Tomatoes": 1500,
    "Milk": 1000,
    "Eggs": 200,
}

print(items)

p = input("Please tell us the item you want: ")

print(f"Okay so you want {p}")

quantity = int(input("How many quantity do you want?: "))

if p in items:
    # both things happen here
    print(items[p])
    print(items[p] * quantity)
else:
    print("Item not found")