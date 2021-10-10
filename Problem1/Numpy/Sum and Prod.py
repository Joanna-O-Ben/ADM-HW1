import numpy

N, M = map(int, input().split())
arr = numpy.array([input().strip().split() for _ in range(N)], int)
s = numpy.sum(arr, axis = 0)
print(numpy.prod(s))


