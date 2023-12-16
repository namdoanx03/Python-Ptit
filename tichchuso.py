# for t in range(int(input())):
#     s = input()
#     res = 1
#     for i in s:
#         if int(i) != 0:
#             res *= int(i)
#     print(res)
def check(s):
    arr = list(int(i) for i in s)
    res = 1
    for i, val in enumerate(arr):
        #hàm enumerate() để lấy cả vị trí và giá trị của từng phần tử. 
        #hàm enumerate() để duyệt qua mảng arr, với i là vị trí và val là giá trị của từng phần tử. Nếu val khác 0,
        if val != 0:
            res *= val
    return res
    
for t in range(int(input())):
    s = input()
    print(check(s))