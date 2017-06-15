def sum(x, y):
    return x + y


print reduce(sum, range(1, 11))
print reduce(sum, range(0, 0), 10)
