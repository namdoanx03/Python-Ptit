def solve(loichuc_list):
    loichuc_khacnhau = set()  # Sử dụng tập hợp để lưu trữ các lời chúc khác nhau

    for loichuc in loichuc_list:
        loichuc_khacnhau.add(loichuc)

    # Số lời chúc khác nhau là số phần tử trong tập hợp
    return len(loichuc_khacnhau)

n = int(input())
loichuc_list = []
#  Tạo một danh sách rỗng loichuc_list để lưu trữ các lời chúc.

for i in range(n):
    loichuc = input().upper()
    loichuc_list.append(loichuc)

print(solve(loichuc_list))
