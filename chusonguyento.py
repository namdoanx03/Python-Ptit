import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

for t in range(int(input())):
    arr = list(int(i) for i in input())
    #tao danh sach cac so nguyen tu chuoi nhap vao
    length = len(arr)
    #do dai cua danh sach so nguyen tren
    nt = 0
    for i in arr:
        nt += isPrime(i) 
    print("YES" if (isPrime(length) and nt > length - nt) else "NO")
    #su dung toan tu 3 ngoi de viet gon cau lenh if else

    