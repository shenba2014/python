class MyFirstClass:
    class InnerClass:
        def run(self):
            print "run from inner class"

    price = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.__count = 1
        isbn = "123"

    def simpleMethod(self):
        print self
        print "current name is", self.name
        print "current color is", self.color

    def outputClassMember(self):
        print "class member price is ", self.price

    @staticmethod
    def getPrice():
        return MyFirstClass.price

    def __getPrice():
        MyFirstClass.price = MyFirstClass.price + 10
        return MyFirstClass.price

    staticGetPrice = staticmethod(__getPrice)

    def __del__(self):
        print "free....", self.name