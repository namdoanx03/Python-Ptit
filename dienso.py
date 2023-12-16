# for i in range(int(input())):
#     n = input()
#     a = list(set(map(int, input().split())))
#     a.sort()
#     print(a[-1] - a[0] - len(a) + 1)
for t in range(int(input())):
    n = int(input())
    a = list(set(map(int, input().split())))
    a.sort()
    print(int(a[-1]) - int(a[0]) + 1 - len(a))
    
    