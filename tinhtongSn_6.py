"""
Chuong trinh tinh tong S(n) = 1/2 + 3/4 + 5/6 + .. + (2n+1)/(2n+2)

"""
n = -1
tong = 0
while (n<=0):
    n = int(input('Nhap n: '))

for i in range(0,n):
    tong = tong + (2*i+1)/(2*i+2)

print('Tong cua day so la: {0}'.format(tong))
