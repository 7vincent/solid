# 1 - SRP - Single Responsibility Principle
#  - Principio da responsabilidade unica;
#  - 1 class apenas com uma responsabilidade;
#  - Como saber se estou ferindo esse principio? Depois de pronto, 
#    se eu precisar mudar, eu mudo mais de uma coisa nela? mais de 
#    um comportamento? se a resposta foi sim, estou feridno esse 
#    principio e atribuindo mais de uma responsabilidade a essa class.

class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.total = 0.0
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
        # self.total += quantity * price

    def calculate_total(self, quantities, prices):
        for quantity, price in zip(quantities, prices):
            self.total += quantity * price
        return self.total
        

    # ... outros métodos relacionados ao pedido ...

class OrderReporter:
    @staticmethod
    def print_order(order):
        for item, quantity, price in zip(order.items, order.quantities, order.prices):
            print(f"{item} x{quantity}: R${price} - Sub-total: R${quantity * price}")
        print(f"Total do pedido: R${order.calculate_total(order.quantities, order.prices) }")
        print(f"Status: {order.status}")

# Uso das classes
order = Order()
order.add_item("Maçã", 5, 1.0)
order.add_item("Banana", 2, 1.5)

reporter = OrderReporter()
reporter.print_order(order)