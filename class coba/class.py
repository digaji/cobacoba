# import grocery <- if this way have to grocery.Grocery
# from grocery import Grocery
from grocery import *  # type: ignore # * <- imports everything
from store import Store  # type: ignore

fish = Grocery("Fish", 50, 3, True, 0.3)  # type: ignore
# print(f"The price after discount: {fish.priceAfterDiscount()}")
# print(f"Buy 100 fishes: {fish.buy(100)}")
# print(f"Total price of every fish is: {fish.totalPrice(True)}")

broccoli = Grocery("Broccoli", 10, 20, True, 0.2)  # type: ignore
cheese = Grocery("Cheese", 200, 5)  # type: ignore
rice = Grocery("Rice", 1, 1000, True, 0.45)  # type: ignore

myStore = Store("Bleb", [broccoli, fish, cheese, rice])
# myStore = Store("Bleb")
# myStore.insertGrocery(broccoli)
# myStore.insertGrocery(fish)
# myStore.insertGrocery(cheese)
# myStore.insertGrocery(rice)

print(f"The total revenue of the store is: {myStore.totalRevenue(True)}")