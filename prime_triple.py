#sang nguyen to
from math import*

MAX = int(1e6)
prime = [True] * (MAX + 1)
def solve():
    prime[0],prime[1] = [False] * 2
    for i in range(2, isqrt(MAX + 1) + 1):
        if prime[i]:
            for j in range(i * i , MAX + 1, i):
                prime[j] = False

for t in range(int(input())):
    n = int(input())
    res = 0
    solve()
    for i in range(2, n -6):
        if prime[i] and (prime[i+2] or prime[i+4]) and prime[i+6]:
            res+=1
    print(res)