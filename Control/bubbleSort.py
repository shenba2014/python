values = [100, 3,5,1,2,34,9]
for i in range(0, len(values)-1):
    for j in range(i+1, len(values)):
        if (values[i] > values[j]):
            t = values[i]
            values[i] = values[j]
            values[j] = t
    print i, values