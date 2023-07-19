"""
Chuong trinh tinh tong S(n) = x + x^2 + x^3 + ... + x^n

"""
import math
n = -1
tong = 0
x = -1

while (x<=0):
    x = int(input('Nhap x>0: '))
while (n<=0):
    n = int(input('Nhap n>0: '))

for i in range(1,n+1):
    tong = tong + pow(x,i)

print('Tong cua day so la: {0}'.format(tong))