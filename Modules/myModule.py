def func():
    print("MyModule.func()")


class MyClass:
    def myFunc(self):
        print("MyModule.MyClas.myFunc()")

count = 1

def getCount():
    global count
    count = count + 1
    return count

if  __name__ == "__main__":
    print "myModule is the main programe"
else:
    print "myMdule is used as a module, and current name is:", __name__
