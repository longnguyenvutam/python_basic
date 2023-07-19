"""
Chuong trinh tinh T(n) = 1*2*3*4*...*n

"""

n = -1
tich = 1

while (n<=0):
    n = int(input('Nhap n > 0: '))

for i in range(1,n+1):
    tich = tich * i

print('Tich cua day so la: {0}'.format(tich))