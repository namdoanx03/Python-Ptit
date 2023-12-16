import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % 2 == 0:
            return False
    return n > 1

for i in range(int(input())):
    a, b = [int(i) for i in input().split()]
    #input().split(): tra ve mot danh sach cac chuoi duoc tach ra tu chuoi nhap
    #vao boi khoang trang
    
    #sau do, cu phap : [int(i) for i in input().split()] : se tao mot danh sach cac so nguyen
    #bang cach chuyen doi tung chuoi trong danh sach thanh so nguyen
    
    #Cuối cùng, cú pháp a, b = [int(i) for i in input().split()] sẽ gán giá trị đầu tiên 
    #của danh sách cho biến a, và giá trị thứ hai cho biến b
    if isPrime(sum(int(i) for i in str(math.gcd(a, b)))):
        #Tính ước chung lớn nhất của a và b bằng hàm math.gcd(a, b)
        #Chuyển kết quả thành một chuỗi bằng hàm str.
        #Tính tổng các chữ số của chuỗi bằng cách duyệt qua từng ký 
        #tự i trong chuỗi, chuyển i thành số nguyên bằng hàm int(i), và cộng dồn vào tổng.
        #Kiểm tra xem tổng có phải là số nguyên tố hay không bằng hàm isPrime.
        print('YES')
    else:
        print('NO')