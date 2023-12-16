for t in range(int(input())):
    s = input() + '!'
    # dấu chấm than giúp code biếts khi nào chuỗi kêt thuc và in ra ket qua day du
    #vì nó không nhận ra rằng chuỗi đã kết thúc và cần in ra số lần xuất hiện của ký tự cuối cùng. 
    
    cnt, ch = 0, s[0]
    for i in s:
        if i == ch:
            cnt = cnt + 1
        else:
            print(str(cnt) + ch, end='')
            cnt, ch = 1, i
    print()