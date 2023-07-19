gioiTinh = ('Nam','Nu') #Khai bao tuple

lopHoc = (1,2,3,4,5,6,7,8,9,10,11,12) #Cac gia tri cua tuple khong thay doi

#Cac phan tu trong tuple co the giong nhau

traiCay = ('Tao','Chuoi','Tao','Cam','Man','Dua Hau')

#Cac thao tac voi tuple

print(gioiTinh[0]) #In phan tu vi tri thu 0

print(traiCay[0:2]) #In phan tu vi tri 0 va 1

y = (1,2,3) + (4,5,6)
print(y) #Gop 2 tuple thanh 1 --> y = (1,2,3,4,5,6)

#Su dung tu khoa in de kiem tra gia tri co ton tai trong tuple khong

print('Bom' in traiCay) # --> False

#Lay so luong phan tu trong tuple --> len
x = len(traiCay)
print(x)  #--> 6

#Dem so lan xuat hien cua 1 phan tu

print(traiCay.count('Tao')) #--> 2

#Neu toan bo phan tu trong tuple la so co the dung ham min,max,sum

print(min(lopHoc))
print(max(lopHoc))
print(sum(lopHoc))

#Sap xep tuple va chuyen ve List

listTC = sorted(traiCay)
print(listTC)



