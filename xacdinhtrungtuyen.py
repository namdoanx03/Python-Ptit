class GV:
    def __init__(self, i, ten, ma, diemTin, diemChuyenMon):
        self.ten = ten
        self.id = 'GV{:02d}'.format(i)
        self.Sj = self.getSubject(ma)
        self.tongDiem = diemTin * 2 + diemChuyenMon  + self.getPriority(ma)
    def getSubject(self, ma):
        if ma[0] =='A': return 'TOAN'
        if ma[0] =='B':return "LY"
        return 'HOA'
    def getPriority(seld, ma):
        if ma[1] == '1': return 2
        if ma[1] == '2': return 1.5
        if ma[1] == '3': return 1
        return 0
    def getStatus(self):
        return 'TRUNG TUYEN' if self.tongDiem >= 18 else  'LOAI'
    def __str__(self) -> str:
        return '{:s} {:s} {:s} {:.1f} {:s}'.format(self.id, self.ten, self.Sj, self.tongDiem, self.getStatus())
list= [] 
for i in range(int(input())):
    list.append(GV(i+1, input(), input(), float(input()), float(input())))
    list.sort(key = lambda x : -x.tongDiem)
for x in list:
    print(x, sep='\n')