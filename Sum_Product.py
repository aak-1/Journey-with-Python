import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))

"""
You are given a 2-D array with dimensions NXN.
Your task is to perform the sum tool over axis 0 and then find the product of that result.
"""