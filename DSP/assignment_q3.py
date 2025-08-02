import numpy as np
A=np.array([[2,3],
            [0,9],
            [-2,-4]
            ])
print("A=\n",A)
B=np.array([[-4,6],
            [23,-7],
            [1,2]
            ])
print("B=\n",B)
print("(a)A+B=\n",A+B)
print("(b)A-B=\n",A-B)
#matrix multiplication
#print("(c)point wise multiplication= \n",np.dot(A,B))-->GIVE ERROR
# print("1st methode=\n",A.dot(B))
# print("2nd methode= \n",np.dot(A,B))
# print("3rd methode=\n",np.matmul(A,B))
# print("4 th methode=\n",A@B)
#print("(d)AB'\n=",A*(np.transpose(B)))#-->THIS GIVES ERROR
print("(e)BA=\n",B*A)