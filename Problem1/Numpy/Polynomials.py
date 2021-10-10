import numpy

P = numpy.array(input().strip().split(), float)
x = int(input())

print(numpy.polyval(P, x))

