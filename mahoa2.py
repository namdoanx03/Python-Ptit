SS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True: # vong lap vo han, neu chuoi nhap vao la 0 thi break
    str = input()
    if str == '0':
        break
    
    k,s = str.split()
    k = int(k)
    res = ''
    for i in s:
        j = SS.find(i)
        # SS.find(i) se tra ve vi tri cua chi so i trong chuoi ss
        #vd i = A thi j = 0
        res += SS[(j+k) % 28]
        #Ký tự mới này được tính bằng cách dịch chuyển chỉ số j sang phải k 
        # vị trí và lấy phần dư khi chia cho 28.
    print(res[::-1])