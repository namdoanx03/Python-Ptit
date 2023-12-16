def solve(s):
    if len(s) < 3:
        #chuoi nho hon 3 tra ve NO
        return "NO"
    arr = list(int(i) for i in s) #list(map(int,s))
    #chuyen chuoi thanh danh sach so nguyen
    increasing = True 
    # biến cờ increasing = True de danh dau trang thai tang hay giam cua day chu so
    for i in range(1, len(arr)):
        # duyet qua tung cap chu so trong danh sach arr, bat dau tu vi tri 1
        # vi vi tri thu 0 khong co chu so truoc no
        if increasing and arr[i] <= arr[i-1]:
            #neu increasing la true , tuc dang o trang thai tang dan , va chu so hien tai nho 
            #nho hon hoac bang chu so truoc no, tuc la chuyen tu trang thai tang dan sang giam dan
            
            #KHI DO bien doi increasing thanh false ,de danh dau trang thai giam dan
            increasing = False
            
        elif not increasing and arr[i] >= arr[i-1]:
            #kiem tra increasing dang o trang thai giam dan, chu so hien tai lon hon hoac bang
            # chu so truoc no , tuc la khong giam dan 
            
            #tra ve NO, vi khong phai tang giam
            return "NO"
        #neu kh dơi vào 2 trường hợp trên thif 
        #tiếp tục duyệt qua các cặp chữ số tiếp theo cho đến hết danh sách.
    return "YES"
#Sau khi duyệt xong danh sách, bạn trả về ‘YES’, vì đã thỏa mãn điều kiện của số tăng giảm.
    
for t in range(int(input())):
    s = input()
    print(solve(s))