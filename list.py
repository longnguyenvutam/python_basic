#Kieu du lieu list
#Tao list rong
emptyList = []
#Tao doi tuong list
emptyList2 = list()

print(emptyList)
print(emptyList2)

color = ['xanh','do','vang']
#Them phan tu vao list
color.append('tim')
#Them phan tu vao list co vi tri
color.insert(2,'luc')
#Dem so luon phan tu thoa dieu kien
color.count('do')
#Xoa phan tu dau tien ra khoi list
color.remove()
#Xoa phan tu ra khoi list va tra ve index cua phan tu do
color.pop('xanh')
#Xoa phan tu ra khoi list co gia tri = vang
color.remove('vang')
#Xoa phan tu ra khoi list = vi tri
color.pop(0)
#Dao nguoc list
color.reverse()
#Sap xep list tu nho den lon
color.sort()
#Sap xep list tu lon den nho
color.sort(reverse=True)
#Xoa het du lieu trong list
color.clear()
