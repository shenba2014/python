import numpy as np
from numpy import array

weight = [1, 1, 1]
height = [2.0, 4.0, 8.0]
bmi = array(weight) / array(height)**2
print bmi
print bmi[bmi < 0.2]

weightAndHeight = array([[1, 1, 1], [2.0, 4.0, 8.0]], dtype=np.int32)
print weightAndHeight
print weightAndHeight[0] / weightAndHeight[1]**2
print 'dataType', weightAndHeight.dtype
print 'shape', weightAndHeight.shape
print 'itemsize', weightAndHeight.itemsize
print 'size', weightAndHeight.size

print 'zero array', np.zeros([2, 2])

print 'rand array', np.random.rand(2, 2)

print 'rand int', np.random.randint(40)

print 'second row'
print weightAndHeight[1, :]

print 'second and third column'
print weightAndHeight[:, 1:3]

print 'the second row and last column'
print weightAndHeight[1, 2]
