n = int(input())
a = list(map(int, input().split()))

res = set(a)
misssing_num = None
for i in range(1, n + 2):
    if i not in res:
        misssing_num = i
        break
print(misssing_num)