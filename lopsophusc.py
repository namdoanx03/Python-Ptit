# Lazygarde

t = int(input())
for k in range(t) :
    a, b, c, d = [int(x) for x in input().split()]
    x = a * a + a * c - b * b - b * d
    y = a * b + b * c + a * b + a * d
    z = (a + c) * (a + c) - (b + d) * (b + d)
    t = 2 * (a + c) * (b + d)
    print(x, end = '')
    if y > 0 : print(' + ', end = '')
    else : print(' - ', end = '')
    print(abs(y), 'i', sep = '', end = '')
    print(',', z, end = '')
    if t > 0 : print(' + ', end = '')
    else : print(' - ', end = '')
    print(abs(t), 'i', sep = '')