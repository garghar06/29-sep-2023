import numpy as np

print(np.__version__)
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
arr0=np.array(42)
print(arr0)

arr1=np.array([1,2,3,4,5])
print(arr1)

arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)

arr3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3)

print("arr0 dim",arr0.ndim)
print("Arr1 dim",arr1.ndim)
print("arr2 dim",arr2.ndim)

