# for t in range(int(input())):
#     n = input()
#     n = n + 'z'
#     ans = -1 # gán cho ans một giá trị âm để đảm bảo rằng giá trị nào cung lơns hơn
#     s = 0
#     for i in range(len(n)):
#         if n[i].isalpha():
#             if i != 0 and n[i-1].isdigit() : 
#                 ans = max(ans, s)
#                 s = 0
#         else:
#             s = s * 10 + int(n[i])
#     print(ans)
    
    
#*thu vien re(regular express) :tim va chich xuat tat ca cac chuoi con chua chữ số từ chuỗi
#dau vao, sau do chuyen cac chuoi thanh các số nguyên và chọn số lơn nháát tu danh sách các số này 

import re

for t in range(int(input())):
    print(max(int(i) for i in re.findall(r'\d+', input())))
    #Ký tự r đặt trước chuỗi biểu thức chính quy '\d+' là để cho Python biết rằng đây là một chuỗi chưa được xử lý (raw string).