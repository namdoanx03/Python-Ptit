f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
# định nghĩa tệp kí tự f, Tập ký tự này sẽ được sử dụng để biểu diễn các chữ số trong các cơ số lớn hơn 10.
for t in range(int(input())):
    n, k = [int(x) for x in input().split()]
    s = ''
    # chuỗi rỗng s để lưu trữ kết quả.
    while (n > 0):
        x = n % k
        s = f[x] + s
        n = int(n / k)
        #Tính phần dư x khi chia n cho k. Phần dư này biểu diễn chữ số bên phải nhất trong biểu diễn cơ số-k.
        #Ghép ký tự tương ứng từ chuỗi f vào đầu chuỗi s dựa trên phần dư x.
        #Cập nhật n bằng cách thực hiện phép chia nguyên (chia lấy phần nguyên) cho k để lấy số thương tiếp theo.
    print(s)