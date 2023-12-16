#Chương trình sẽ sử dụng đệ quy để tạo tất cả các xâu ký tự có độ dài từ 3 đến n mà 
# thỏa mãn yêu cầu về việc chứa cả ba ký tự A, B, C và số lượng A không nhiều hơn số lượng B, số lượng B không nhiều hơn số lượng C.

def Try(s, n, a, b, c):
    if len(s) == n and a > 0  and a <= b and b <= c:
        print(s)
    if len(s) < n:
        Try(s + 'A', n, a + 1, b, c)
        Try(s + 'B', n, a, b + 1, c)
        Try(s + 'C', n, a, b, c + 1)


n = int(input())
for i in range(3, n + 1):
    Try('', i, 0, 0, 0)  