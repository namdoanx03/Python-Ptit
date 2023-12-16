def check(s):
    for i in s:
        if s < '0' or i > '2':
            #s < '0':neu chuoi co ki tu khong phai la so
            #i > '2:neu chuoi co ki tu lon hon 2
            return "NO"
    return "YES"

for t in range(int(input())):
    s = input()
    print(check(s))