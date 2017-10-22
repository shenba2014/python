from numpy import mat
mat1 = [[2,4,6,8]]
mat2 = [[2,3,2,2]]
print mat(mat1).T
print mat(mat1).T * mat2
mat3 = [[2,5],[5,10]]
print mat(mat3)
print mat(mat3).I