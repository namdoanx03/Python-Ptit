import  math

def check(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i ==0:
            return "NO"
    return "YES" if n > 1 else "NO"

for t in range(int(input())):
    s = sum(int(i) for i in input())
    print(check(s))