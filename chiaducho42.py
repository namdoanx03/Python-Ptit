test = 10
ls = []
while test > 0:
    data = input()
    base = data.split()
    for i in base:
        tmp = int(i) % 42
        if not tmp in ls:
            ls.append(tmp)
    test -= len(base)
print(len(ls))