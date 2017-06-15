def arithmetic(x=1.0, y=1, operator="+"):
    result = {"+": x + y, "-": x - y, "*": x * y, "/": x / y}
    return result.get(operator)


print arithmetic(y=4, operator="/")


def arithmeticWithArgs(args=[], operator="+"):
    x = args[0]
    y = args[1]
    result = {"+": x + y, "-": x - y, "*": x * y, "/": x / y}
    return result.get(operator)


print arithmeticWithArgs([1, 3])


def sumArgs(*args):
    return sum(args)


print sumArgs(1, 3, 5)
