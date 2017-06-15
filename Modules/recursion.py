def reFunc(n):
    if (n <= 0):
        return 0
    if (n == 1):
        return 1
    else:
        print "recursion at", n
        return reFunc(n - 1) * n


print reFunc(1)
print reFunc(3)
print reFunc(5)

print "recurrsion by function reduce"
multiply = lambda x, y: x * y
print "5! =", reduce(multiply, range(1, 6))
