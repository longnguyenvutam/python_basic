#Giai phuong trinh bac 2
import math

a = float((input('Nhap vao so a: ')))
b = float((input('Nhap vao so b: ')))
c = float(input('Nhap vao so c: '))

if(a!=0):
    delta = b**2 - 4 * a * c
    if (delta<0):
        print("Phuong trinh vo nghiem")
    elif (delta == 0):
        x = -b/(2*a)
        print('Phuong trinh co nghiem kep x1 = x2 = {0}'.format(x))
    else:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print('Phuong trinh co 2 nghiem x1 = {0} , x2 = {1} '.format(x1,x2))
else:
    print('Khong phai phuong trinh bac 2')