#行列の四則演算
#参考文献
#https://www.headboost.jp/python-numpy-array-calculations/

import numpy as np
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[2, 5], [1, 3]])

print("計算する行列\narray1 = \n", array1)
print("\n\array2 = \n", array2)
array3 = array1 + array2 #足し算

print("\narray1 + array2 =")
print(array3)

print("\narray1 - array2 = ")
array4 = array1 - array2 #引き算
print(array4) 

print("\narray1 * array2 = ")
array5 = np.matmul(array1, array2) #掛け算
print(array5) 

print("\narray1 / array2 = ")
array6 = np.linalg.inv(array2) #逆行列を計算
array7 = np.matmul(array1, array6) #割り算（逆行列を掛ける）
print(array7)