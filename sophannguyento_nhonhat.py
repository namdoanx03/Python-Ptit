# def so_luong_uoc_so(n):
#     cnt = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             cnt += 1
#     return cnt

# def phan_nguyen_to_nho_nhat(x):
#     num = x + 1
#     while True:
#         num_divisors = so_luong_uoc_so(num)
#         x_divisors = so_luong_uoc_so(x)
        
#         if num_divisors > x_divisors:
#             return num 
#         num += 1
# for t in range(int(input())):
    
#     x = int(input())
#     print(phan_nguyen_to_nho_nhat(x))

import sys
from bisect import bisect_left
X = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
test = int(input())
i = 0
for line in sys.stdin:
    n = int(line)
    print(X[bisect_left(X,n)])
    i += 1
    if i == test: break