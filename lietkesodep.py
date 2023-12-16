def isValid(s):
    if len(s) % 2 == 1 or s != s[::-1]:#dao nguoc chuoi s
        return False
    for i in s:
        if int(i) % 2 == 1:
            return False
    return True

for t in range(int(input())):
    n = int(input())
    for i in range(22, n, 2):#duyet qua cac gia tri cua bien i tu 22 den n-1 , buoc nhay 2
        if isValid(str(i)):
            print(i, end = ' ')
    
    print()