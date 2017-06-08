def incomeTax(income):
    shouldTaxAmount = income - 3500
    tax = 0
    if (shouldTaxAmount <= 0):
        return 0
    if shouldTaxAmount > 80000:
        tax = tax + (shouldTaxAmount - 80000) * 0.45
        shouldTaxAmount = 80000
    if shouldTaxAmount > 55000:
        tax = tax + (shouldTaxAmount - 55000) * 0.35
        shouldTaxAmount = 55000
    if shouldTaxAmount > 35000:
        tax = tax + (shouldTaxAmount - 35000) * 0.30
        shouldTaxAmount = 35000
    if shouldTaxAmount > 9000:
        tax = tax + (shouldTaxAmount - 9000) * 0.25
        shouldTaxAmount = 9000
    if shouldTaxAmount > 4500:
        tax = tax + (shouldTaxAmount - 4500) * 0.20
        shouldTaxAmount = 4500
    if shouldTaxAmount > 1500:
        tax = tax + (shouldTaxAmount - 1500) * 0.10
        shouldTaxAmount = 1500
    if shouldTaxAmount <= 1500:
        tax = tax + shouldTaxAmount * 0.03
    return tax


income = input('please input your income:')
income = float(income)
print "your income tax is:", incomeTax(income)