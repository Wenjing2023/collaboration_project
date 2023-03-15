from models.order import *

# order = Order("Name", "Item", "Quantity", "Description", "Date")
order1 = Order("Thomas", "game", 1, "SuperMario", "20 Feb")
order2 = Order("Wenjing", "food", 6, "Fuji red big juicy apples", "20 Aug")
order3 = Order(
    "Sky",
    "book",
    2,
    "CSS is fun!",
    "15 Mar",
)

orders = [order1, order2, order3]
