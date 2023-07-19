"""
Chuong trinh kiem tra so hoan thien

"""

n = -1
tong = 0 
while (n<0):
    n = int(input('Nhap so nguyen duong n > 0: '))

for i in range(1,n):
    if(n % i == 0):
        tong = tong + i

if (tong == n):
    print('{0} la so hoan thien'.format(n))
else:
    print('{0} khong phai la so hoan thien'.format(n)) 