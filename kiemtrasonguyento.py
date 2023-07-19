'''
Chuong trinh kiem tra so nguyen to

'''

n = -1
m = 0
while(n<0):
    n = int(input('Nhap so nguyen duong n > 0: '))

for i in range(2,n):
    if(n % i == 0 ):
        m += 1

if (m>0):
    print('{0} khong phai la so nguyen to'.format(n))
else:
    print('{0} la so nguyen to'.format(n))