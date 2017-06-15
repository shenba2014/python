def doubleMap(x):
    return x * 2


print map(doubleMap, range(1, 11))

myTuple = (23, "ccc", 34, "bbb")
a, b, c, d = myTuple
print a, b, c, d


def power(x, y):
    return x**y


print map(power, range(1, 5), range(5, 1, -1))

print zip(range(1, 5), range(4, 8))
