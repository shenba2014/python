import numpy as np
a1 = np.random.normal(1.75, 0.2, 10)
a2 = np.random.normal(60.32, 15, 10)
print np.column_stack((a1, a2))