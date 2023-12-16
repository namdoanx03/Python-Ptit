for t in range(int(input())): 
    #lap qua so luong bo test qua ban phim
    arr = list(int(i) for i in input())
    #ham input de nhan 1 chuoi nhan tu ban phim
    #ham for de duyet qua cac ki tu trong chuoi
    #int de chuyen cac ki tu thanh cac so nguyen
    #ham list de tao 1 danh sach tu cac so nguyen do
    for i in range(len(arr) - 1, 0, -1):
        #lap qua cac gia tri tu len(arr)-1 den 1 , buoc nhay 0
        if arr[i] >= 5:
            #kiem tra xem neu tai i(hang don vi) >= 5 thi tang tai vi tri i -1 (hang chuc ) len 1 don vi,sau do gan tai vi tri i (don vi) = 0
            arr[i - 1] = arr[i - 1] + 1
        arr[i] = 0
    if arr[0] == 10:
        arr[0] = 0
        arr = [1] + arr
        # neu so dau tien bang 10 thi gan so dau tien bang 0 va them so 1 vao dau danh sach
    for i in arr:
        print(i, end='')
        #bien i de duyet qua cac phan tu trong danh sach arr, print de in gia tri cua i, end='' de khong xuong dong
    print()
    #in ra 1 dong trong de phan cach cac bo test