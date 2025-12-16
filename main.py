# 1. Do'kon klassi
class Store:
    def __init__(self, name, location, products=None):
        self.name = name
        self.location = location
        self.products = products if products else []

    def add_product(self, product):
        self.products.append(product)

    def __str__(self):
        return f"Do'kon: {self.name}, Manzil: {self.location}, Mahsulotlar: {self.products}"


# 2. Bank hisobi klassi
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Balans yetarli emas"
        self.balance -= amount

    def __str__(self):
        return f"Egasi: {self.owner}, Balans: {self.balance}"



