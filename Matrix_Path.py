import numpy as np


def Martix_Path(Matrix):
    
    ans = np.zeros(shape = (4,4), dtype=np.int8)
    ans[0][0] = Matrix[0][0]
    for i in range(1, Matrix.shape[0]):
        
        ans[i][0] = Matrix[i][0] + ans[i-1][0]
    
    for j in range(1, Matrix.shape[1]):
        ans[0][j] = Matrix[0][j] + ans[0][j-1]
        
    for i in range(1, Matrix.shape[0]):
        for j in range(1, Matrix.shape[1]):
            ans[i][j] = Matrix[i][j] + max(ans[i-1][j], ans[i][j-1])
    return ans
        
        
        
print("Start")        
Matrix = np.array([[6,7,12,5],
                 [5,3,11,18],
                 [7,17,3,3],
                 [8,10,14,9]])

print(Martix_Path(Matrix))