import math

def find_shortest_subarray(arr, k):
    n = len(arr)
    min_length = math.inf
    start = -1

    for i in range(n):
        gcd = arr[i]
        if gcd == k:
            return 1
        for j in range(i+1, n):
            gcd = math.gcd(gcd, arr[j])
            if gcd == k:
                length = j - i + 1
                if length < min_length:
                    min_length = length
                    start = i

    if min_length == math.inf:
        return -1
    else:
        return min_length

# Đọc số lượng bộ test
t = int(input())

# Xử lý từng bộ test
for _ in range(t):
    # Đọc độ dài và giá trị K
    n, k = map(int, input().split())

    # Đọc dãy số A
    arr = list(map(int, input().split()))

    # Tìm độ dài dãy con ngắn nhất
    result = find_shortest_subarray(arr, k)

    # In kết quả
    print(result)