# def check_min_max(p, q, X):
#     min_sum = max_sum = 0

#     for x in X:
#         min_x = int(x.replace(p, q))
#         max_x = int(x.replace(q, p))
        
#         min_sum += min(min_x, max_x)
#         max_sum += max(min_x, max_x)

#     return min_sum, max_sum

# T = int(input())  # Đọc số lượng bộ test

# for _ in range(T):
#     p, q = input().split()  # Đọc p và q
#     X1 = input()  # Đọc số X1
#     X2 = input()  # Đọc số X2
    
#     X = [X1, X2]
    
#     min_sum, max_sum = check_min_max(p, q, X)
    
#     print(min_sum, max_sum)  # In ra kết quả cho từng bộ test
for t in range(int(input())):
    n, m = input().split()
    ip = input().split()
    if len(ip) == 1:
        str1 = ip[0]
        str2 = input()
    else:
        str1, str2 = ip
    num1 = int(str1.replace(n, m)) + int(str2.replace(n, m))
#     Số lượng bộ test T: 1
# Dòng tiếp theo chứa hai số nguyên n và m: 5 và 6
# Dòng tiếp theo chứa chuỗi ip: "645"
# Tiếp theo, chương trình sẽ thực hiện các phép thay thế theo các bước được mô tả trong mã:

# Thay thế tất cả các xuất hiện của n (số 5) trong chuỗi "645" bằng m (số 6), kết quả là chuỗi "646". Chuyển đổi kết quả thành số nguyên: 646.
# Thay thế tất cả các xuất hiện của m (số 6) trong chuỗi "646" bằng n (số 5), kết quả là chuỗi "545". Chuyển đổi kết quả thành số nguyên: 545.
    num2 = int(str1.replace(m, n)) + int(str2.replace(m, n))
#     Tương tự cho str2:

# Thay thế tất cả các xuất hiện của n (số 5) trong chuỗi "666" bằng m (số 6), kết quả là chuỗi "666".
# Thay thế tất cả các xuất hiện của m (số 6) trong chuỗi "666" bằng n (số 5), kết quả là chuỗi "555".

# Sau đó, chương trình tính tổng của num1 và num2:
    print(min(num1, num2), max(num1, num2))