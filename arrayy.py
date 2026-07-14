#one dimensional array.
import numpy as np
arr=np.array([10,20,30,40])
print(arr)

#two dimensional array.
arr=np.array([[1,2,3],[4,5,6]])
print(arr)

#array properties.
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

#array indexing dimensional.
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[0])
print([2])
print([-1])

#two dimensional indexing.
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr[0,1])
print(arr[1,2])

#mathematical operations.
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+5)
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#universal functions.
import numpy as np
arr=np.array([1,4,9,16])
print(np.sqrt(arr))
print(np.square(arr))
print(np.sin(arr))
print(np.cos(arr))

#aggregate functions.
arr=np.array([10,20,30,40])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))

#array sorting.
arr=np.array([50,20,10,40])
print(np.sort(arr))

#boolean sorting.
arr=np.array([5,10,15,20,25])
print(arr[arr>15])