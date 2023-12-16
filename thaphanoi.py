def thapHaNoi(n,a,b,c):
    if n == 1:
        print(a, '->', c)
    else:
        thapHaNoi(n-1, a, c, b)
        print(a, '->', c)
        thapHaNoi(n-1, b, a, c)
thapHaNoi(int(input()),"A","B","C")