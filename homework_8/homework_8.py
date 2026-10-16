class Flower:
    def __init__(self, name, price, lifetime):
        self.name = name
        self.price = price
        self.lifetime = lifetime


class Rose(Flower):
    def __init__(self):
        super().__init__("Роза", 170, 7)


class Tulip(Flower):
    def __init__(self):
        super().__init__("Тюльпан", 140, 4)


class Lily(Flower):
    def __init__(self):
        super().__init__("Лилия", 210, 6)


class Daisy(Flower):
    def __init__(self):
        super().__init__("Ромашка", 80, 3)


class Accessory:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def get_total_cost(self):
        total = 0

        for flower in self.flowers:
            total += flower.price

        for accessory in self.accessories:
            total += accessory.price

        return total

    def get_wilting_time(self):
        if not self.flowers:
            return 0

        total_lifetime = 0

        for flower in self.flowers:
            total_lifetime += flower.lifetime

        return total_lifetime / len(self.flowers)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def has_flower(self, name):
        for flower in self.flowers:
            if flower.name == name:
                return True

        return False


bouquet = Bouquet()

bouquet.add_flower(Rose())
bouquet.add_flower(Tulip())
bouquet.add_flower(Lily())
bouquet.add_flower(Rose())

bouquet.add_accessory(Accessory("Лента", 70))
bouquet.add_accessory(Accessory("Топпер", 150))
bouquet.add_accessory(Accessory("Упаковка", 200))

print("Стоимость букета:", bouquet.get_total_cost())
print("Среднее время жизни:", bouquet.get_wilting_time(), "дней")

bouquet.sort_by_cost()

print("Цветы по стоимости:")
for flower in bouquet.flowers:
    print(flower.name, "—", flower.price)

print("Роза в букете:", bouquet.has_flower("Роза"))
print("Ромашка в букете:", bouquet.has_flower("Ромашка"))
