for t in range(int(input())):
    s = input()
    res = ''
    
    for i in range(0, len(s), 2):#duyet cac gia tri cua bien i tu 0 den do dai cua chuoi s-1, buoc nhay la 2
        res += s[i] * int(s[i+1])
        #lay ki tu tai vi tri i trong s
        #lay ki tu tai vi tri i + 1 trong s , chuyen thanh so nguyen
        # nhan ki tu voi so nguyen , roi cong vao chuoi ket qua res 
        #sau khi duyet xong thi in ra chuoi ket qua s
    print(res)