import math

for t in range(int(input())):
    n,x,m = [float(i) for i in input().split()]
    #cau truc list comprehension
    #cu phap: [expression for variable in iterable],
    #trong do :expression là biểu thức tính toán giá trị của mỗi phần tử,
    #variable là biến lặp qua các phần tử của iterable, và iterable là một đối tượng có thể lặp được như chuỗi, danh sách, hoặc tập hợp
    #Trong trường hợp này, expression là float(i), tức là chuyển đổi chuỗi i thành số thực, variable là i, và iterable là input().split(),
    # tức là một danh sách các chuỗi được tách ra từ input bằng dấu cách.
    #Ví dụ, nếu input là ‘100 10 200’,
    # thì [float(i) for i in input().split()] sẽ trả về [100.0, 10.0, 200.0], và n = 100.0, x = 10.0, m = 200.0.
    res = math.log(m / n, 1 + x / 100)
    print(math.ceil(res))
    #math.ceil(a) là hàm làm tròn số thực a lên số nguyên gần nhất.