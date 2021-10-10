import numpy


N, M = map(int, input().split())
arr = numpy.array([input().strip().split() for _ in range(N)], int)
# arr = numpy.around(arr,decimals=11)
m = numpy.mean(arr, axis = 1)
v = numpy.var(arr, axis = 0)
s = numpy.std(arr, axis = None)

print(m)
print(v)
print(round(s, 11))