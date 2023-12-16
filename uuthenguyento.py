import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 :
            return 0
    return n > 1
for t in range(int(input())):
    s = input()
    nt = 0
    for i in s:
        if isPrime(int(i)):
            nt += 1
    print("YES" if isPrime(len(s)) and nt > len(s) - nt else "NO")