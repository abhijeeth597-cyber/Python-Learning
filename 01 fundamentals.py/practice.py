class chai:
    def __init__(self,  name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

tea = chai("Garam chai", 20, 200)
print(f"{tea.name} costs {tea.price} rupees per cup, and the quantity is {tea.quantity}ml per cup")
