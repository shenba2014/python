import myModule
from myModule import *
from myModule import func
import sys

func()

myClass = MyClass()
myClass.myFunc()

print "call get count in myModule"
print myModule.getCount()

print "set mymodule.count as 10"
myModule.count = 10

print "import mymodule again"
import myModule
print myModule.getCount()

print "just output __doc__"
print __doc__