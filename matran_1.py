n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

k  = int(input())
nuaTren, nuaDuoi = 0, 0

for i in range(n):
    for j in range(n):
        if j > i:
            nuaTren += a[i][j]
        elif j < i:
            nuaDuoi += a[i][j]
"""
VD:
1 2 3
4 5 6 
7 8 9

>i = 0: Lần duyệt đầu tiên (hàng đầu)

Vòng lặp bên trong (j) duyệt từ 0 đến n-1 (0 đến 2):
j = 0: Kiểm tra xem j > i. Trong trường hợp này, 0 > 0 là Sai, vì vậy chúng ta bỏ qua vòng lặp này.
j = 1: Kiểm tra xem j > i. Trong trường hợp này, 1 > 0 là Đúng, vì vậy chúng ta cộng a[0][1] vào nuaTren: nuaTren += 2.
j = 2: Kiểm tra xem j > i. Trong trường hợp này, 2 > 0 là Đúng, vì vậy chúng ta cộng a[0][2] vào nuaTren: nuaTren += 3.
i = 1: Lần duyệt thứ hai (hàng giữa)

Vòng lặp bên trong (j) duyệt từ 0 đến n-1 (0 đến 2):
j = 0: Kiểm tra xem j > i. Trong trường hợp này, 0 > 1 là Sai, vì vậy chúng ta bỏ qua vòng lặp này.
j = 1: Kiểm tra xem j > i. Trong trường hợp này, 1 > 1 là Sai, vì vậy chúng ta bỏ qua vòng lặp này.
j = 2: Kiểm tra xem j > i. Trong trường hợp này, 2 > 1 là Đúng, vì vậy chúng ta cộng a[1][2] vào nuaTren: nuaTren += 6.
i = 2: Lần duyệt thứ ba (hàng cuối)

Vòng lặp bên trong (j) duyệt từ 0 đến n-1 (0 đến 2):
j = 0: Kiểm tra xem j > i. Trong trường hợp này, 0 > 2 là Sai, vì vậy chúng ta bỏ qua vòng lặp này.
j = 1: Kiểm tra xem j > i. Trong trường hợp này, 1 > 2 là Sai, vì vậy chúng ta bỏ qua vòng lặp này.
j = 2: Kiểm tra xem j > i. Trong trường hợp này, 2 > 2 là Sai, vì vậy chúng ta bỏ qua vòng lặp này.
"""

if abs(nuaTren - nuaDuoi) <= k:
    print("YES")
else:
    print("NO")
print (abs(nuaDuoi-nuaTren))