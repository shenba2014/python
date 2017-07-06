from firstClass import MyFirstClass

if __name__ == "__main__":
    myFirstObj = MyFirstClass("python", "yellow")
    myFirstObj.simpleMethod()

    MyFirstClass.price = MyFirstClass.price + 1
    myFirstObj.outputClassMember()

    print id(myFirstObj.price)
    print id(MyFirstClass.price)

    print "access private member", myFirstObj._MyFirstClass__count