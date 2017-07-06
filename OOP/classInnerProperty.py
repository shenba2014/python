from firstClass import MyFirstClass
from secondClass import MySecondClass

if __name__ == "__main__":
    myfirstObj = MyFirstClass("python", "yellow")
    mySecondObj = MySecondClass("python2", "yellow")
    print "base class of MyFirstClass", MyFirstClass.__bases__
    print "properties in myfirstObj", myfirstObj.__dict__
    print "module name of myfirstObj", myfirstObj.__module__
    print "doc of myfirstObj", myfirstObj.__doc__

    print "base class of MySecondClass", MySecondClass.__bases__
    print "properties in mySecondObj", mySecondObj.__dict__
    print "module name of mySecondObj", mySecondObj.__module__
    print "doc of mySecondObj", mySecondObj.__doc__

    print "call static method", MyFirstClass.getPrice()
    print "call static method by using staticmethod function", MyFirstClass.staticGetPrice(
    )

    print "create instance of inner class"

    innerObj = MyFirstClass.InnerClass()
    innerObj.run()

    print "I can call constructor method, it sounds cool", myfirstObj.__init__(
        "python", "red")
