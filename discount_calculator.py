def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Check if the discount is 20% or more
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return original price if discount is less than 20%

# Get user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and print final price
final_price = calculate_discount(price, discount_percent)
print(f"Final price after discount (if applicable): ${final_price:.2f}")


