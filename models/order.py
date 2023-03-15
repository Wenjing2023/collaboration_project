class Order:
    def __init__(
        self,
        customer_name,
        item,
        quantity,
        description,
        order_date,
    ):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.item = item
        self.description = description
