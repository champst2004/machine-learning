import numpy as np

arr = np.array([-1, 2, 5], dtype=np.float32)
print(repr(arr))

arr1 = np.array([[0, 1, 2], [3, 4, 5]],dtype=np.float32) # matrix
print(repr(arr1))


# copying
a = np.array([0, 1])
b = np.array([9, 8])
print('Array a: {}'.format(repr(a)))
d = b.copy()
print('Array d: {}'.format(repr(d)))
d[0] = 10
print('Array d: {}'.format(repr(d)))



arr2 = np.array([np.nan, 'abc'])
print(repr(arr2))


arr3 = np.array([np.inf, 5])
print(repr(arr3))

arr4 = np.array([-np.inf, 1])
print(repr(arr4))

arr4 = arr4.astype(np.float32)
print(arr4.dtype)