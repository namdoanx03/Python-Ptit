for t in range(int(input())):
    n = int(input())
    sum = 0
    for i in range(2 - n % 2, n+1, 2 ):
        #2 - n%2 : neu n chan thi bat dau tu 2
        # neu n le thi 2-1 =1 , bat dau tu 1
        sum += 1/i
    print('{:.6f}'.format(sum))