s = input()
lower = 0

for i in s:# duyet tung ki tu i trong s
    if i.islower():#islower la mot phuong thuc cua doi tuong chuoi trong python
        lower = lower + 1
        
if lower >= len(s) - lower:
        print(s.lower())
else:
        print(s.upper())