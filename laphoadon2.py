from datetime import datetime

class HoaDon:
    def __init__(self , i, ten, phong, ngayNhan, ngayTra, dichVu) -> None:
        self.id = 'KH{:02d}'.format(i)
        self.ten = ten
        self.phong = phong
        time = datetime.strptime(ngayTra, '%d/%m/%Y') - datetime.strptime(ngayNhan, '%d/%m/%Y')
        self.days = time.days + 1
        self.dichVu = dichVu
    def tongPhi(self):
        if self.phong[0] == '1': return 25 * self.days + self.dichVu
        if self.phong[0] == '2': return 34 * self.days + self.dichVu
        if self.phong[0] == '3': return 50 * self.days + self.dichVu
        if self.phong[0] == '4': return 80 * self.days + self.dichVu
    def __str__(self) -> str:
        return f'{self.id} {self.ten} {self.phong} {self.days} {self.tongPhi()}'
    
list=[]
for i in range(1, int(input()) + 1):
    list.append(HoaDon(i, input().strip(), input().strip(),input().strip(), input().strip(), int(input().strip())))
list.sort( key = lambda x : -x.tongPhi()) 
for k in list:
    print(k, sep='\n')      
        
        