import numpy
numpy.set_printoptions(legacy = '1.13')

A = numpy.array(input().strip().split(), float)
print(numpy.floor(A), sep = ' ', end = '\n')
print(numpy.ceil(A), sep = ' ', end = '\n')
print(numpy.rint(A), sep = ' ', end = '\n')