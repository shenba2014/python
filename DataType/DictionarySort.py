dic = {"a": "book", "b": "apple"}
print dic
print "sort by key"
print sorted(dic.items(), key=lambda d: d[0])
print "sort by value"
print sorted(dic.items(), key=lambda d: d[1])
