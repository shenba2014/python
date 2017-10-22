from numpy import random
from numpy import mat
from numpy import eye
from numpy import array
a = random.rand(2, 2)
print 'use random to generate a 2*2 array\n', a
print 'and conver it to 2*2 matrix\n', mat(a)
print 'and the inverse of matrix\n', mat(a).I
unitMatrix = mat(a) * mat(a).I
print 'original matrix multiply inverse of matrix\n', unitMatrix
print 'matrix created from eye(2)', eye(2)
print 'subtract matrix from eye(2)', unitMatrix - eye(2)
list = ['a','b','c']
print array(list)