from math import*

def isPrime(n):
    if n < 2 :
        return False
    for i in range (2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(str):
    for i in str:
        if not isPrime(int(i)):
            return 'No'
    s = sum([int(i) for i in str])
    num1, num2 = str, str[::-1]
    if not isPrime(s) or not isPrime(int(num1)) or not isPrime(int(num2)):
        return 'No'
    return 'Yes'

for t in range(int(input())):
    n = int(input())
    print(solve(str(n)))