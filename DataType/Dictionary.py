dic = {"a": "apple", "b": "book"}
print("%s, %(a)s, %(b)s" % dic)
print "pop in dictioanry"
print dic.pop("a", 2)
print dic.pop("a1", 2)
print "loop using for .. in"
for k in dic:
    print("dic[%s]=" % k, dic[k])
print "return keys"
print dic.keys()
print "return values"
print dic.values()
print "update dic with other dic"
dic1 = {"a": "iphone", "c": "category"}
dic.update(dic1)
print dic
print "set default for dic"
dic2 ={}
dic2.setdefault("a")
print dic2
dic2["a"] = "apache"
print dic2