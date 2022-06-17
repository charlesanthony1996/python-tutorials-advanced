#array broadcasting in numpy

import numpy as np

x= np.array([[0], [1], [2]])
y = np.array([[3, 4, 5]])

print(x)
print(y)

print()
print(x+ y)

print(x.shape == (2, 3))
print(y.shape == (2, 1))
print(y.shape == (1, 3))
print(y.shape == (3,))



print(y.shape == (3, 2))
print(y.shape == (3, 2))
print(y.shape == (2,))




x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

y= np.array([1, 10, 100]).reshape(3, 1)

print()

print(x + y)
shape = (3, 3)
out = np.empty(shape, dtype=int)
N0, N1 = shape
for i in range(N0):
    for j in range(N1):
        #in the dimension that y only has 1 element , just use it
        out[i, j]= x[i, j] + y[i, 0]
print(out)

print()


x = np.array([[[0, 1, 2], [3,4, 5], [6, 7, 8]], [[9, 10, 11], [12, 13, 14], [15, 16, 17]]])

y = np.array([1, 10, 100])

print(x + y)

shape = (2, 3, 3)
out = np.empty(shape, dtype=int)
N0, N1 , N2 = shape
for i in range(N0):
    for j in range(N1):
        for k in range(N2):
            out[i, j, k] =x[i, j , k] + y[k]

print(out)



#both arrays can have broadcasted axes not just one


#exercise

y = np.array([2, 3, 4]).reshape(3, 1, 1)

x = np.ones(shape,dtype=np.uint8)
shape = (1000, 3, 32, 32)

out = np.empty(shape, dtype=np.uint8)

N, C, W, H = shape
for n in range(N):
    for channel in range(C):
        for w in range(W):
            for h in range(H):
                out[n, channel , w, h] = x[n, channel, w, h] * y[0, channel, 0, 0]

