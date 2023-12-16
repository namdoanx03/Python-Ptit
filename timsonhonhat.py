for t in range(int(input())):
    n = input()
    n = n + 'z' # them ki tu 'z' vao cuoi chuoi de dam bao rang vong lap xu li den ki tu cuoi cung
                #cua chuoi n
    ans = 10 ** 20 #gan ans = gia tri lon 
    s = 0
    for i in range(len(n)):
        if n[i].isalpha(): # neu ki tu tai vi tri la mot chu cai, ki tu truoc  no (n[i-1]) 
                            # la mot chu so.neu dung cap nhat gia tri ans = min (ans,s) 
            if i != 0 and n[i-1].isdigit() : ans = min(ans,s) 
            #Sau khi xử lý xong một chuỗi liên tiếp các chữ số, biến s được đặt lại thành 0.
            s = 0
        else:s = s*10 + int(n[i])
        #Nếu ký tự tại vị trí i là một chữ số (không phải chữ cái), chương trình cập nhật giá trị của s bằng cách 
        # nhân s hiện tại với 10 và cộng thêm giá trị số tương ứng với ký tự này.
    print(ans)