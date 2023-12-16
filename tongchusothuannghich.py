for t in range(int(input())):
    s = str(sum(int(i) for i in input()))
    print("YES" if len(s) > 1 and s == s[::-1] else "NO")
    