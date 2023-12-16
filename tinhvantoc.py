from datetime import datetime

class VanToc:
    def __init__(self, ten, donVi, time_arrive):
        self.ten = ten
        self.donVi = donVi
        self.time_arrive = time_arrive
        self.id = self.getID(ten,donVi)
        time = datetime.strptime(time_arrive, '%H:%M') - datetime.strptime('6:00', '%H:%M')
        self.speed = 120 / time.seconds * 3600 # chia cho so time roi nhan voi 3600s
    def getID(self, ten, donVi) -> str:
        return ''.join([i[0:1].upper() for i in donVi.split()]) + ''.join([i[0:1].upper() for i in ten.split()])
    def __str__(self) -> str:
        return f"{self.id} {self.ten} {self.donVi} {round(self.speed)} Km/h"
list=[]
for _ in range(int(input())):
    list.append(VanToc(input(), input(), input()))
    list.sort(key = lambda x : -x.speed)
for i in list:
    print(i, sep='\n')