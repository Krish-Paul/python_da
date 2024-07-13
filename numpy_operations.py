import numpy as np
##############for more operations visit            https://numpy.org/doc/stable/reference/routines.linalg.html

list1=[1,2,3,4,5]
np1=np.array(list1)
np1

type(np1)

list2=[5,6,7,8,9]
np2=np.array([list1,list2])
np2

np2.shape

np2.size#no of elements

np2.dtype

np.identity(n=5)

np.eye(3,3)

np.zeros([4,3])

np2[0,3]

np2[0:,2:]

np2[::-1,::-1]

np.reshape(np2,(5,2))

np2.flatten()

np2.T

np2.transpose()

np.flipud(np2)

np.fliplr(np2)

np.rot90(np2,k=3)

np2+100#similarly use all math operations to each element without using loop

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[3,4],[5,6]])
arr1+arr2#similarly use all math operations

np.std(np2)

np.mean(np2)

np.mean(np2,axis=1)

np.sum(np2)

np.log(np2 )

np.sqrt(np2)

np.dot(arr1,arr2)
