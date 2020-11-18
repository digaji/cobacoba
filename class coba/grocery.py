class Grocery:
    def __init__(self, name, price, quantity, isOnSale=False, salePercentage=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.isOnSale = isOnSale
        self.salePercentage = salePercentage  # Any float from 0 - 1

    def priceAfterDiscount(self) -> float:
        if self.isOnSale:  # If on sale
            return (1 - self.salePercentage) * self.price
        else:  # If not on sale
            return self.price

    def buy(self, qty):
        if qty > self.quantity: # If amount of items being bought greater than in stock -> clamp the qty
            qty = self.quantity
        self.quantity -= qty
        return qty * self.priceAfterDiscount()

    def totalPrice(self, countAsSale) -> float:
        if countAsSale:
            return self.quantity * self.priceAfterDiscount()
        else:
            return self.quantity * self.price