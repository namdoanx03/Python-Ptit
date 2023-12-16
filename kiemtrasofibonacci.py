for t in range(int(input())):
    f = [1] * 93
    for i in range(3,93):
        if f[i] == f[i-1] + f[i-2]:
            print("YES")
        else:
            print("NO")