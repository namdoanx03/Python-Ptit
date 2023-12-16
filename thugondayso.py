n = input()
A = list(map(int, input().split()))
#ham map() de ap dung ham int cho tung phan tu cua danh sach input().split()

i = 1

while i < len(A):
    if (A[i] + A[i-1]) % 2 == 0:
        A.pop(i)
        #pop() : xoa phan tu
        A.pop(i-1)
        if i > 1:
            i  -= 1
    else:
            i += 1
print(len(A))
#Giả sử danh sách ban đầu là [1, 2, 4, 6, 3, 5, 7, 8]. Ta khởi tạo i = 1 và bắt đầu vòng lặp.

#Bước 1: i = 1. Kiểm tra xem cặp [1, 2] có tổng chẵn hay không. Có, vì (1 + 2) % 2 == 0. Vậy ta xóa cả hai phần tử này khỏi danh sách. Danh sách sau khi xóa là [4, 6, 3, 5, 7, 8]. Kiểm tra xem i có lớn hơn 1 hay không. Không, vì i = 1. Vậy ta không giảm i đi.
# Bước 2: i = 1. Kiểm tra xem cặp [4, 6] có tổng chẵn hay không. Có, vì (4 + 6) % 2 == 0. Vậy ta xóa cả hai phần tử này khỏi danh sách. Danh sách sau khi xóa là [3, 5, 7, 8]. Kiểm tra xem i có lớn hơn 1 hay không. Không, vì i = 1. Vậy ta không giảm i đi.
# Bước 3: i = 1. Kiểm tra xem cặp [3, 5] có tổng chẵn hay không. Không, vì (3 + 5) % 2 == 1. Vậy ta không xóa gì cả. Tăng i lên thành i = 2.
# Bước 4: i = 2. Kiểm tra xem cặp [5, 7] có tổng chẵn hay không. Không, vì (5 + 7) % 2 == 1. Vậy ta không xóa gì cả. Tăng i lên thành i = 3.
# Bước 5: i = 3. Kiểm tra xem cặp [7, 8] có tổng chẵn hay không. Có, vì (7 + 8) % 2 ==0. Vậy ta xóa cả hai phần tử này khỏi danh sách. Danh sách sau khi xóa là [3,5]. Kiểm tra xem i có lớn hơn hay không. Có, vì i =3 >1. Vậy ta giảm i đi thành i =2.
# Bước 6: i =2. Kiểm tra xem cặp [3,5] có tổng chẵn hay không. Không, vì (3 +5) %2 ==1. Vậy ta không xóa gì cả. Tăng i lên thành i =3.
# Bước cuối: i =3 >= len(list) =3. Điều kiện của vòng lặp không còn thỏa mãn nữa, nên ta thoát khỏi vòng lặp.
# Sau khi thoát khỏi vòng lặp, ta in ra độ dài của danh sách list hiện tại là len(list) =3.