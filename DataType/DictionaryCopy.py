import copy
dic = {"a": "book", "b": {"g": "grape", "o": "orange"}}
dic2 = copy.deepcopy(dic)
dic3 = copy.copy(dic)
dic2["b"]["g"] = "book1"
print dic
dic3["b"]["g"] = "apple1"
print dic