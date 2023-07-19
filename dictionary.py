"""
Luu tru gia tri du lieu trong cac cap key:value
Tap hop duoc sap xep theo thu tu
Co the thay doi va khong duoc trung lap key

Khai bao bang dau { }

"""

sinhVien = {
    "hoVaTen" : "Nguyen Van A",
    "maLop" : "DH01",
    "diemTrungBinh" : 8.5
}

print(sinhVien["hoVaTen"])

#Su dung get() de lay gia tri

print(sinhVien.get("maLop"))

#Thay doi gia tri

sinhVien["maLop"] = "DH02"

#Thay doi gia tri = phuong thuc update()

sinhVien.update({"maLop" : "DH03"})

#Them muc moi

sinhVien["namHoc"] = 2023
sinhVien.update({"noiSinh" : "Vung Tau", "namSinh" : 1992})
print(sinhVien)

#Xoa key:value
#Phuong thuc pop() truyen vao key

sinhVien.pop('noiSinh')

#Phuong thuc popitem() xoa cap key:value cuoi cung

sinhVien.popitem()

print(sinhVien)

#Lam trong dictionary

sinhVien.clear()

#In tat ca gia tri

for x in sinhVien:
    print(x)

#Duyet cac values
for x in sinhVien.values():
    print(x)

#Duyet cac key
for x in sinhVien.keys():
    print(x)

#Duyet cac cap key:value
for key,value in sinhVien.items():
    print(key,value) 