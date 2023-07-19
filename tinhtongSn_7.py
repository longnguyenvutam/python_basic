"""
Chuong trinh tinh tong S(n) = 1 + 1*2 + 1*2*3 + ... + 1*2*3*...*n

"""

n = -1
tong = 0
tich = 1
while (n<=0):
    n = int(input('Nhap n > 0: '))

for i in range(1,n+1):
    tich = 1
    for y in range(1,i+1):
        tich = tich*y
    tong = tong + tich

print('Tong cua day so la: {0}'.format(tong))   