import numpy as np
A=np.array([[1+1j,2-1j,3],
            [0,9+2j,8],
            [-2+1j,-4,1-1j]])
print(A)
print("(a)determinant of A=\n",np.linalg.det(A))
print("(b)conjugate of A=\n",np.conjugate(A))
print("(c)Transpose of A=\n",np.transpose(A))
print("(d)Hermitian matrix of A=\n",np.conjugate(A.T))
print("(e)Inverse of A=\n",np.linalg.inv(A))