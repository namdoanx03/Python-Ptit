import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):#n chia cho cac so tu 2 den can hai cua n , neu chia het cho bat ki so nao thi false , va nguoc lai
        if n % i == 0:
            return False
    return n > 1


for t in range(int(input())):
    n = int(input())
    k = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            #uoc so chung lon nhat cua n va i la 1
            k = k + 1
    if isPrime(k):
        print('YES')
    else:
        print('NO')
