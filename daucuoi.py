for t in range(int(input())):
    s = input()
    if s[0] == s[len(s)-2] and s[1] == s[len(s) - 1]:
            print('YES')
    else:
            print("NO")
    