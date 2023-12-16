# from math import *

# def nt(n):
#     if n < 2:
#         return False
#     for i in range (2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# n = int(input())
# a = list(map(int,input().split()))

# cnt = {}
# for i in a:
#     if nt(i):
#         if i in cnt:
#             cnt[i] += 1
#         else:
#             cnt[i] = 1
# for i in cnt:
#     print(str(i) + " " + str(cnt[i]))

from collections import Counter
import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))

res = Counter(a)
for key, value in res.items():
    if isPrime(key):
        print(key, value)