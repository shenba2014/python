def func(n):
    for i in range(n):
        yield i

for i in func(10):
    print i

r = func(10)
print r.next()
print r.next()