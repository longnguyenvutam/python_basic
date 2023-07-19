"""
Chuong trinh tinh tong S(n) = 1/2 + 1/4 + 1/6 + ... + 1/2n

"""

n = -1
tong = 0
while(n<=0):
    n = int(input('Nhap n: '))
for i in range(1,n+1):
    tong = tong + 1/(2*i)

print('Tong cua day so la: {0}'.format(tong))

