
class ngayThangNam:

    def __init__(self,ngay,thang,nam):
        self.ngay = ngay
        self.thang= thang
        self.nam = nam

    def getNgay(self):
        return self.ngay
    
    def setngay(self,ngay):
        self.ngay = ngay

    def getThang(self):
        return self.thang
    
    def setThang(self,thang):
        self.thang = thang

    def getNam(self):
        return self.nam
    
    def setNam(self,nam):
        self.nam = nam


class tacGia(ngayThangNam):
    def __init__(self,tenTacGia,ngay,thang,nam):
        ngayThangNam.__init__(self,ngay,thang,nam)
        self.tenTacGia = tenTacGia

    def getTenTacGia(self):
        return self.tenTacGia
    
    def setTenTacGia(self,tenTacGiaMoi):
        self.tenTacGia = tenTacGiaMoi


class Sach(tacGia):

    def __init__(self,tenSach, giaBan, namXuatBan,tenTacGia):
        self.tenTacGia = tenTacGia
        self.tenSach = tenSach
        self.giaBan = giaBan
        self.namXuatBan = namXuatBan

    
    def getTenSach(self):
        return self.tenSach
    
    def getGiaBan(self):
        return self.giaBan
    
    def getNamXuatBan(self):
        return self.namXuatBan
    
    def setTenSach(self,tenSachMoi):
        self.tenSach = tenSachMoi

    def setGiaBan(self,giaBanMoi):
        self.giaBan = giaBanMoi

    def setNamXuatBan(self,namXuatBanMoi):
        self.namXuatBan = namXuatBanMoi

    def inTenSach(self):
        print("Ten sach la: {0}".format(self.tenSach))

    def kiemTraCungNamXuatBan(self,b):
        if self.namXuatBan == b.getNamXuatBan():
            return True
        else:
            return False

    def giaSauKhiGiamGia(self,gia):
        return self.giaBan *(1-(gia/100))
    

ngay1 = ngayThangNam(15,5,2023)
ngay2 = ngayThangNam(15,6,2022)
ngay3 = ngayThangNam(15,7,2022)

tacGia1 = tacGia("Long IT",ngay1.getNgay,ngay1.getThang,ngay1.getNam)
tacGia2 = tacGia("Long Nguyen",ngay2.getNgay,ngay2.getThang,ngay3.getNam)
tacGia3 = tacGia("Long NVT",ngay3.getNgay,ngay3.getThang,ngay3.getNam)

sach1 = Sach("Lap trinh C", 5000, 2023, tacGia1.getTenTacGia)
sach2 = Sach("Lap trinh Java", 10000, 2023,tacGia2.getTenTacGia)
sach3 = Sach("Lap trinh mang", 15000,2023,tacGia3.getTenTacGia)

sach1.inTenSach()
sach2.inTenSach()
sach3.inTenSach()

print("So sanh NXB sach 1 va 3: {0}".format(sach1.kiemTraCungNamXuatBan(sach3)))

print("Sach 1 giam 10%: {0}".format(sach1.giaSauKhiGiamGia(10)))
print("Sach 2 giam 20%: {0}".format(sach2.giaSauKhiGiamGia(20)))
print("Sach 3 giam 30%: {0}".format(sach3.giaSauKhiGiamGia(30)))
    



        
    