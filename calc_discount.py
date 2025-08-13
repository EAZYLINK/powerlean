def calculate_discount(price, discount_percent):
    final_price = 0
    if discount_percent >= 20:
        final_price = price * (1 - (discount_percent / 100))
    else: final_price = price
    print(final_price)