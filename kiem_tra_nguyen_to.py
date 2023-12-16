# import math


# def prime(n):
#     if n < 2:
#         return 0
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return 0
#     return 1


# n, m = [int(i) for i in input().split()]
# for i in range(n):
#     list = [prime(int(i)) for i in input().split()]
#     print(*list)
import math

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

n, m = map(int, input().split())
a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(n):
    for j in range(m):
        print(isPrime(a[i][j]), end=" ")
    print()