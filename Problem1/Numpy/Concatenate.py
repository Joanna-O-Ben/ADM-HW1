import numpy

N, M, P = map(int, input().split())

arr_n = numpy.array([input().strip().split() for _ in range(N)], int)
arr_m = numpy.array([input().strip().split() for _ in range(M)], int)

ar_N = numpy.reshape(arr_n, (N, P))
ar_M = numpy.reshape(arr_m, (M, P))

print(numpy.concatenate((ar_N, ar_M), axis = 0))