"""
Chuong trinh ting tong S(n) = 1+2+3+...+n

"""
n = -1
tong = 0
while (n<=0):
    n = int(input('Nhap n: '))
for i in range(1,n+1):
    tong = tong+i
print('Tong cua day so la: {0}'.format(tong)) 
