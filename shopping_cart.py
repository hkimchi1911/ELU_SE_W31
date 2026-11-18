def calculate_total(cart):
    total = 0.0
    for item in cart:
        total += float(item['price'])
    return total


def display_total(total):
    print(f"Total price: ${total:.2f}")


cart = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': '8.49'}
]

for item in cart:
    print(f"Item: {item['name']} - Price: ${float(item['price']):.2f}")

shopping_cart_total = calculate_total(cart)
display_total(shopping_cart_total)

