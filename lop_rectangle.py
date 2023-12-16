from math import*
class Rectangle:
    def __init__(self,dai, rong, mau_sac):
        self.dai = dai
        self.rong = rong
        self.mau_sac = mau_sac
    def perimeter(self):
        return 2 * ( self.rong + self.dai)
    def area(self):
        return self.dai * self.rong
    def color(self):
        return self.mau_sac.capitalize()
        
arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color())) 
else:
    print("INVALID")