import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
numpy.set_printoptions(legacy='1.13')
print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(numpy.std(A, axis=None))


"""
You are given a 2-D array of size NXM.
Your task is to find:

The mean along axis 1
The var along axis 0
The std along axis None
"""