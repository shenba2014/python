def isPrimeNumber(number):
    for i in range(2, number - 1):
        if (number % i == 0):
            return False
    return True

def getPrimeNumber(number):
    for i in range(2, number):
        if (isPrimeNumber(i)):
            print i

getPrimeNumber(100)