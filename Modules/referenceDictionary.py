def search(*t, **d):
    keys = d.keys()
    values = d.values()
    print keys
    print values
    for arg in t:
        if (d.__contains__(arg)):
            print "key ", arg, " find, value is ", d[arg]


search("one", "three", one = 1, two = 2, three = 3)
