import numpy

N, M = map(int, input().split())
arr = numpy.array([input().strip().split() for _ in range(N)], int)
m = numpy.min(arr, axis = 1)
print(numpy.max(m))
