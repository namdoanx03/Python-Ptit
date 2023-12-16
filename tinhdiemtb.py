import math
from math import ceil
class SinhVien:
    def __init__(self, id,name, s1, s2, s3) -> None:
        self.id =  'SV{:02d}'.format(id)
        self.name = self.formatName(name)
        self.score= (s1 * 3 + s2 * 3 + s3 * 2) / ( 3+3+ 2)
    def formatName(self, name):
        return ' '.join(i.title() for i in name.strip().split())
    def __str__(self) -> str:
        return '{:s} {:s} {:.2f} {:d}'.format(self.id, self.name, ceil(self.score * 100) / 100, self.rank)
    
list  = []
for i in range(int(input())):
    list.append(SinhVien(i+1, input(), float(input()), float(input()), float(input())))
list.sort(key = lambda x : (-x.score, x.id))
list[0].rank = 1
for i in range(1, len(list)):
    list[i].rank = list[i-1].rank if list[i].score == list[i-1].score else i + 1
print(*list, sep ='\n') 