import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

for t in range(int(input())):
    s = input()
    print("YES" if isPrime(int(s[0:3])) and isPrime(int(s[-3:])) else "NO")
    