# if __name__ == "__main__":
#     t = int(input())
#     while t > 0:
#         n, k = [int(x) for x in input().split()]
#         solve = [int(x) for x in input().split()]
#         l = []
#         r = []
#         biggest = max(solve)
#         for i in range(n):
#             if solve[i] == biggest:
#                 solve.insert(i, k)
#                 break
#         for i in range(len(solve)):
#             if solve[i] >= 0:
#                 r.append(solve[i])
#             else: l.append(solve[i])
#         print(" ".join(str(x) for x in l), end = " ")
#         print(" ".join(str(x) for x in r))
#         t -= 1

for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = max(a)
    l= []
    r= []
    for j in range(n):
        if a[j]  == res:
            a.insert(j, k)
            break
    for i in range(len(a)):
        if a[i] >= 0:
            r.append(a[i])
        else:
            l.append(a[i])
    print(" ".join(str(x) for x in l), end=" ")
    print(" ".join(str(x) for x in r))