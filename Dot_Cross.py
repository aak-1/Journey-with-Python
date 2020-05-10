import numpy

a=int(input())

arr1=numpy.array([list(map(int,input().split())) for _ in range(a)])

arr2=numpy.array([list(map(int,input().split())) for _ in range(a)])

print(numpy.dot(arr1,arr2))

"""
You are given two arrays A and B. Both have dimensions of N.
Your task is to compute their matrix product.
"""