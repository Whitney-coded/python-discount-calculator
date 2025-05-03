def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    Apply the discount only if discount_percent is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * discount_percent / 100
        return price - discount_amount
    else:
        return price

def main():
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    final_price = calculate_discount(price, discount_percent)
    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price is: {price:.2f}")

if __name__ == "__main__":
    main()
