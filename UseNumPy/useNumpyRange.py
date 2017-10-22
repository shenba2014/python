import numpy as np
npRange = np.arange(1, 11)
print 'arange', npRange
print 'arange reshap'
reshapedRange = npRange.reshape(2, 5)
print reshapedRange
print 'exp for a range'
print np.exp(reshapedRange)
print 'sqrt for a range'
print np.sqrt(reshapedRange)

print 'sum example by axis 0'
print np.sum(reshapedRange, axis=0)
print 'sum example by axis 1'
print np.sum(reshapedRange, axis=1)

print 'max example by axis 0'
print np.max(reshapedRange, axis=0)
print 'max example by axis 1'
print np.max(reshapedRange, axis=1)

print 'oper two list'
list1 = np.array([10, 20, 30, 40])
list2 = np.array([4, 3, 2, 1])
print 'Add'
print list1 + list2
print '**'
print list1 * list2
print 'dot matrix mul'
print np.dot(list1.reshape(2,2), list2.reshape(2,2))