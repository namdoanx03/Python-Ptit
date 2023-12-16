class HoaDon:
    def __init__(self, ma, ten, soluong, dongia, chietkhau) -> None:
        self.ma = ma
        self.ten = ten
        self.soluong = soluong
        self.dongia = dongia
        self.chietkhau = chietkhau
    def getTongTien(self):
        return self.soluong * self.dongia - self.chietkhau
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {self.soluong} {self.dongia} {self.chietkhau} {self.getTongTien()}'
list =[]
for i in range (int(input())):
    list.append(HoaDon(input().strip(), input().strip(), int(input()), int(input()), int(input())))
    list.sort(key = lambda x: -x.getTongTien())
for x in list:
    print(x, sep= '\n')