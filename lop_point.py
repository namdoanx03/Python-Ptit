from math import*
import math
class Point:
    def __init__(self,x, y ):
        self.x = x
        self.y = y
    def distance(self, other):
        #Phương thức này tính toán và trả về khoảng cách Euclidean giữa điểm hiện tại (self) và một điểm khác (other).
        d = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return f'{d:.4f}'
def Decimal(n):
    return float(n)
#Hàm này chuyển đổi giá trị của n thành kiểu dữ liệu số thực (float)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1