class Store:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products

    def insertGrocery(self, grocery):
        self.products.append(grocery)

    def totalRevenue(self, countAsSale):
        result = 0
        for item in self.products:
            result += item.totalPrice(countAsSale)
        return result