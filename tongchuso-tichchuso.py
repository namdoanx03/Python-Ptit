for t in range(int(input())):
    a = list(int(i) for i in input())
    su, mu = 0, 0
    for i in range(len(a)):
        if i % 2 == 0:
            su += a[i]
        else:
            if a[i] != 0: #neu gia tri cua a[i] khac 0
                if mu == 0:#neu mu bang 0, 
                              #thiet lap gia tri cua mu thanh gia tri cua a[i]
                    mu = a[i]
                else: #neu mu khac 0, nhan gia tri cua a[i] voi mu
                    mu *= a[i]
    print(str(su) + " " + str(mu))