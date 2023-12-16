import math

n, k = [int(i) for i in input().split()]
count = 0
lower, upper = 10 ** (k-1), 10 ** k

for i in range(lower, upper):
    if math.gcd(n,i) == 1:
        print(i, end = ' ')
        count += 1
        if count % 10 == 0: #neu count chia het cho 10 thi xuong dong de in ra cac so cach nhau boi khoang trang
            print()