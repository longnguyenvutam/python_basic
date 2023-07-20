"""
Chuong trinh tim phan so nho nhat tao ra tu 3 so nhap vao
In ra tong cua tu so va mau so cua phan so nho nhat 

Vi du: 3 2 4
Ta co cac phan so: 3/2 3/4 2/3 2/4 4/3 4/2

Phan so nho nhat : 2/4 = 1/2
--> 1 + 2 = 3

"""
a = b = c = 0
a1 = b1 = c1 = 0
a2 = b2 = c2 = 0
a3 = b3 = c3 = 0
a4 = b4 = c4 = 0
a5 = b5 = c5 = 0

while(a <= 0 or a > 1000 ):
    a = int(input('Nhap so a: '))

while(b <= 0 or b > 1000):
    b = int(input('Nhap so b: '))

while(c <= 0 or c > 1000):
    c = int(input('Nhap so c: '))

danhSachPhanSo = list() #Khai bao list

a1 = a2 = a3 = a4 = a5 = a
b1 = b2 = b3 = b4 = b5 = b
c1 = c2 = c3 = c4 = c5 = c

for i in range(1):
    #Rut gon phan so
    if(b1 % a1 == 0):
        b1 = b1 / a1
        a1 = a1 / a1       
     #Them cac phan so tao ra tu 3 so nhap vao vao list
    danhSachPhanSo.append(a/b)

for i in range(1):
    if(c1 % a2 == 0):
        c1 = c1 / a2
        a2 = a2 / a2
    danhSachPhanSo.append(a/c)

for i in range(1):
    if(a3 % b2 == 0):
        a3 = a3 / b2
        b2 = b2 / b2
    danhSachPhanSo.append(b/a)

for i in range(1):
    if(c3 % b3 == 0):
        c3 = c3 / b3
        b3 = b3 / b3
    danhSachPhanSo.append(b/c)

for i in range(1):
    if(a4 % c4 == 0):
        a4 = a4 / c4
        c4 = c4 / c4
    danhSachPhanSo.append(c/a)

for i in range(1):
    if(b5 % c5 == 0):
        b5 = b5 / c5
        c5 = c5 / c5
    danhSachPhanSo.append(c/b)

phanSoNhoNhat = min(danhSachPhanSo)
for i in range(6):
    if(phanSoNhoNhat == danhSachPhanSo[i]):
        index = i
    
print('Phan so nho nhat la: {0}'.format(phanSoNhoNhat))

#In ra danh sach cac phan so
#for i in range(6):
#   print(danhSachPhanSo[i])

#In ra tong cua 2 so tao ra phan so nho nhat
tong = 0
if(index==0):
    tong = a1+b1
    print('Tong cua 2 so tao nen phan so nho nhat la {0}/{1} = {2}: '.format(a,b,tong))
elif(index==1):
    tong = a2+c1
    print('Tong cua 2 so tao nen phan so nho nhat la {0}/{1} = {2}: '.format(a,c,tong))
elif(index==2):
    tong = b2+a3
    print('Tong cua 2 so tao nen phan so nho nhat la {0}/{1} = {2}: '.format(b,a,tong))
elif(index==3):
    tong = b3+c3
    print('Tong cua 2 so tao nen phan so nho nhat la {0}/{1} = {2}: '.format(b,c,tong))
elif(index==4):
    tong = c4+a4
    print('Tong cua 2 so tao nen phan so nho nhat la {0}/{1} = {2}: '.format(c,a,tong))
else:
    tong = c5+b5
    print('Tong cua 2 so tao nen phan so nho nhat la {0}/{1} = {2}: '.format(c,b,tong))

