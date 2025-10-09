class Product :
    def __init__ (self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total(self):
        result = self.price * self.quantity
        print(f"The total is: {result}")
        return result
    