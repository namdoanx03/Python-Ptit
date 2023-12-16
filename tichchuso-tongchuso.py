for t in range(int(input())):
    arr = list(int(i) for i in input())
    su,res = 0, 1
    for i in range(len(arr)):
        if arr[i] != 0:
            if i % 2 != 0:
                su += arr[i]
            else:
                res *= arr[i]
    print(str(res) +" "+ str(su)) 