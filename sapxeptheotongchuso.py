# from math import*
# def tong(n):
#     res = 0
#     while n != 0:
#         res += n%10
#         n //= 10
#     return res
            
# if __name__=="__main__":
#     for t in range(int(input())):
#         n = int(input())
#         a = list(map(int, input().split())) 
#         a.sort(key= lambda x : (tong(x), x)) 
#         for x in a:
#             print(x, end=" ")
#         print()
import math
def solve( n):
    return (int(i) for i in str(n))
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x: (solve(x), x))
    for x in a:
        print(x, end=" ")
    print()
