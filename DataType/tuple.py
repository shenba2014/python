tuple = ("apple", "banana", "grape", "orange")
print "tuple[0]", tuple[0]
print "type(tuple)", type(tuple)
print "tuple[-1]", tuple[-1]
print "tuple[-2]", tuple[-2]
print "tuple[2:-2]", tuple[1:-2]

print "concat two tuples"
book1 =("asp", "java")
book2 =("php", "pyphon")
bookTuple = (book1, book2)
print bookTuple
print "bookTuple[0][0]", bookTuple[0][0]
print "print by loop"
for i in range(len(bookTuple)):
    print ("tuple[%d] :" %i, "",)
    for j in range(len(bookTuple[i])):
        print (bookTuple[i][j], "", )
    print()
print "print by for...in"
for i in bookTuple:
    for j in i:
        print j
