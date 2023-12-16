from datetime import datetime

class MonHoc:
    def __init__(self, id, ten):
        self.id = id
        self.ten = ten
    
    def __str__(self):
        return f'{self.id} {self.ten}'

class LichThi:
    def __init__(self, id, monhoc, ngay, thoigian, nhomthi):
        self.id = 'T{:03d}'.format(id)
        self.monhoc = monhoc
        self.ngay = ngay
        self.thoigian = thoigian
        self.nhomthi = nhomthi
    
    def __str__(self):
        return f'{self.id} {str(self.monhoc)} {self.ngay} {self.thoigian} {self.nhomthi}'

n, m = [int(i) for i in input().split()]
monHoc = [MonHoc(input(), input()) for _ in range(n)]
lichthi = []

for i in range(m):
    s = input().split()
    sjId = s[0]
    for sj in monHoc:
        if sj.id == sjId:
            lichthi.append(LichThi(i+1, sj, s[1], s[2], s[3]))
            break

lichthi.sort(key=lambda x: (datetime.strptime(x.ngay, '%d/%m/%Y'), datetime.strptime(x.thoigian, '%H:%M'), x.id))
print(*lichthi, sep='\n')