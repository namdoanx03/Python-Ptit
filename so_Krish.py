F = [1] * 10 
#  mảng đánh dấu 10 phần tử có giá tri bằng 1 
for i in range(2, 10):
    F[i] = F[i-1] * i
    # tính giá trị của từng mảng
    
for t in range(int(input())):
    n = input()
    s = sum(F[int(i)] for i in n)
    print('Yes' if int(n) == s else 'No')