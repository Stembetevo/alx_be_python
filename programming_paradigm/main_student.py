from product import Product

def main():
    # Create a product instance
    product = Product("Laptop", 999.99, 2)
    
    # Calculate and display the total price
    product.calculate_total()
    print(f"Product Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
    print(f"Total price of the product {product.name} is {product.calculate_total()}")
    

