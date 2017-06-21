from functools import reduce
import operator
strs = ["hello ", "world ", "hello ", "china "]
result = reduce(operator.add, strs, "")
print result