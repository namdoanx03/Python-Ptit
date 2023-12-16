def solve(s):
    n = 0
    for i in s:
        n += ord(i) - ord('0')
    return str(n)


s = input()
cnt = 0
while(len(s) > 1):
    s = solve(s)
    cnt += 1
print(cnt)
    
    