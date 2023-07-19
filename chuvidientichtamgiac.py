"""
Nhap 2 diem tren he truc toa do 0xy
0.Xac dinh 3 diem co tao thanh tam giac hay khong
1. Neu tao thanh tam giac
    1.a Xuat ra chu vi
    1.b Xuat ra dien tich
"""

#Nhap du lieu
import math

xA = float(input('Nhap vao xA: '))
yA = float(input('Nhap vao yA: '))
xB = float(input('Nhap vao xB: '))
yB = float(input('Nhap vao yB: '))
xC = float(input('Nhap vao xC: '))
yC = float(input('Nhap vao yC: '))

ab = math.sqrt(math.pow((xB-xA),2) + math.pow((yB-yA),2))
bc = math.sqrt(math.pow((xC-xB),2) + math.pow((yC-yA),2))
ac = math.sqrt(math.pow((xC-xA),2) + math.pow((yC-yA),2))

#Kiem tra tong 1 canh phai lon hon canh con lai
if(ab+bc > ac) and (ab+ac > bc) and (ac+bc > ab):
    #Tinh chu vi tam giac
    cv = ab + ac + bc
    print('Chu vi = {0} '.format(cv))

    #Tinh dien tich tam giac
    #Cong thu heron
    p = cv/2
    s = math.sqrt(p * (p-ab) * (p-bc) * (p-ac))
    print('Dien tich = {0}'.format(s))
else:
    print('Khong tao thanh tam giac')