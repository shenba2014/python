class Fruit:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def getColor(self):
        return self.__color

    def getName(self):
        return self.__name


class FruitShop:
    def __init__(self):
        self.fruits = []

    def addFruit(self, fruit):
        fruit.parent = self
        self.fruits.append(fruit)