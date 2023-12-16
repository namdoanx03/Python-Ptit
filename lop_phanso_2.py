from math import*

class PhanSo:
    def __init__(self,tu, mau):
        self.tu = tu
        self.mau = mau
    def toi_gian(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def cong(self, other):
        #tính mẫu số mới bằng cách nhân mẫu số của self với mẫu số của other sau đó chia cho ước chung lớn nhất của hai mẫu số
        #tính tử số mới bằng cách tính tử số của self và other theo mẫu số mới và tạo ra một đối tượng PhanSo mới
        #Cuối cùng, chúng ta rút gọn phân số kết quả và trả về đối tượng đó.
        mau = self.mau * other.mau // gcd(self.mau, other.mau)
        tu = self.tu * (mau // self.mau) + other.tu * (mau // other.mau)
        result = PhanSo(tu, mau)
        result.toi_gian()
        return result
if __name__=="__main__":
    a, b, c, d = map(int, input().split())
    p = PhanSo(a, b)
    q = PhanSo(c, d)
    tong = p.cong(q)
    print(f'{tong.tu} / {tong.mau}')