def filterFunc(x):
    if x > 0:
        return x


print filter(filterFunc, range(-9, 10))
print list(filter(filterFunc, range(-9, 10)))
