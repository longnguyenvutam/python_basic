"""
Chuong trinh ting tong S(n) = 1 + 1/3 + 1/5 + ... + 1/2n+1

"""

n = -1
tong = 1
while(n<=0):
    n = int(input('Nhap n: '))

for i in range(1,n+1):
    tong = tong + 1/(2*i+1)

print('Tong cua day so la: {0}'.format(tong))

