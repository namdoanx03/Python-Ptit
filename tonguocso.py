# import math

# sumAll = 0

# for t in range(int(input())):
#     n = int(input())
#     factors_sum = 0
        
#     for i in range(2, int(math.sqrt(n) + 1)):
            
#         while n % i == 0:
#             factors_sum += i
#             n //= i
#         if n == 1:
#             break
            
#     if n > 1:
#         factors_sum += n
#     sumAll += factors_sum
# print(sumAll)
# Sàng Eratosthenes để tìm ước số nguyên tố
b = [0]*(2*10**6+5)
b[0]=1
b[1]=1
for i in range(2,2*10**6+5):
    if b[i]==0:
        for j in range(2*i,2*10**6+5,i):
            b[j]=i
        b[i]=i
s=0
for _ in range(int(input())):
    a = int(input())
    while(a>1):
        s=s+int(b[a])
        a=a//b[a]

print(s)