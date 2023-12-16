for t in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    new_arr = a[d:] + a[:d] 
    # a[d:]: lay cac phan tử từ vị trí d đến cuối danh sách
    # a[:d]: lay các phần tử từ đầu đến vị trí d - 1
    for i in new_arr:
        print(i, end=" ")
    print()