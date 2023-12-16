# for t in range(int(input())):
#     n= int(input())
#     a= list(map(int, input().split()))
    
#     cnt = {}
#     app_max = 1
#     num = float('inf') 
#     """
#     so duong vo cung
#     """ 
#     for i in a:
#         if i not in cnt:
#             cnt[i] = 1
#         else:
#             cnt[i] += 1
            
#     app_max = max(cnt.values())
#     # kiem tra xem so lan xuat hien nhieuf nhat cua danh sach
#     for f, s in cnt.items():
#             if s == app_max:
#                 # neu so lan xuat hien s cua f thi f la mot trong cac so co so lan xuat hien nhieu nhat trong dah sach
                
#                 num = min(num, f)
#             # dieu kien tren dung chung to s = app_max, thi ddong nay so sanh f voi num 
#             # -> dieu nay dam bao rang num luu tru so nho nhat trong cac 
#             #so co so lan xuat hien nhieu nhat
                
#     if app_max > n // 2:
#         print(num)
#     else:
#         print("NO")
from collections import Counter

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)

    max_freq = max(freq.values())  # Tần số xuất hiện lớn nhất trong danh sách

    if max_freq > n / 2:
        result = min([num for num, count in freq.items() if count == max_freq]) # list comprehension
        #freq.items() trả về một danh sách các cặp (key, value) trong freq, trong đó key là giá trị và value là tần số xuất hiện tương ứng.
        # Khi duyệt qua mỗi cặp (num, count), nếu count bằng max_freq, thì num sẽ được chọn và thêm vào danh sách.
        print(result)
    else:
        print("NO")