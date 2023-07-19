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

