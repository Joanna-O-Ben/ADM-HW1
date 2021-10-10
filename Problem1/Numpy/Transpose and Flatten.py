import numpy

N, M  = map(int, input().split())

arr = [input().strip().split(' ') for _ in range(N)]
ar = numpy.array(arr, int)
a = numpy.reshape(ar, (N, M))

print(numpy.transpose(a))
print(a.flatten())