import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(A, axis=1), axis=0))


"""
You are given a 2-D array with dimensions NXN.
Your task is to perform the min function over axis 1 and then find the max of that.
"""