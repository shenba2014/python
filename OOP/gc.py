import gc
from firstClass import MyFirstClass
from Fruit import FruitShop
from Fruit import Fruit


if __name__ == "__main__":
    shop = FruitShop()
    shop.addFruit(Fruit("apple", "red"))
    shop.addFruit(Fruit("banana", "yellow"))
    print gc.get_referrers(shop)