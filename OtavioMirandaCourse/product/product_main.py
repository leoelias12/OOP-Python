class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percent):
        self.price = self.price - (self.price * (percent / 100))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.title().strip()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$', ''))

        self._price = value


p1 = Product('   MUg.', 'R$10')
p1.discount(50)
print(p1.name, p1.price)
