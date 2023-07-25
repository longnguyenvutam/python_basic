class Ngay:

    def __init__(self,ngay,thang,nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def getNgay(self):
        return self.ngay
    
    def getThang(self):
        return self.thang
    
    def getNam(self):
        return self.nam
    
    def setNgay(self,ngay):
        self.ngay = ngay

    def setThang(self,thang):
        self.thang = thang

    def setNam(self,nam):
        self.nam = nam

    
class hangSanXuat:

    def __init__(self, tenHangSanXuat, quocGia):
        self.tenHangSanXuat = tenHangSanXuat
        self.quocGia = quocGia

    def getTenHangSanXuat(self):
        return self.tenHangSanXuat
    
    def getQuocGia(self):
        return self.quocGia
    
    def setTenHangSanXuat(self,tenHangSanXuat):
        self.tenHangSanXuat = tenHangSanXuat

    def setQuocGia(self,quocGia):
        self.quocGia = quocGia
    
class boPhim(hangSanXuat,Ngay):

    def __init__(self,tenPhim,namSanXuat,tenHangSanXuat,quocGia,giaVe,ngay,thang,nam):
        hangSanXuat.__init__(self,tenHangSanXuat,quocGia)
        Ngay.__init__(self,ngay,thang,nam)
        self.tenPhim = tenPhim
        self.namSanXuat = namSanXuat
        self.giaVe = giaVe

    def getTenPhim(self):
        return self.tenPhim

    def getNamSanXuat(self):
        return self.namSanXuat

    def getGiaVe(self):
        return self.giaVe
    
    def setTenPhim(self,tenPhim):
        self.tenPhim = tenPhim

    def setNamSanXuat(self,namSanXuat):
        self.namSanXuat = namSanXuat

    def setGiaVe(self,giaVe):
        self.giaVe = giaVe

    def giaSauKhuyenMai(self,gia):
        return self.giaVe * (1-(gia/100))
    
    def kiemTraGiaVe(self,gia):
        if self.getGiaVe() < gia:
            return True
        else:
            return False
    

ngay1 = Ngay(15,5,2022)
ngay2 = Ngay(31,1,2025)
ngay3 = Ngay(16,2,2023)


hangSanXuat1 = hangSanXuat("Hang 1","Viet Nam")
hangSanXuat2 = hangSanXuat("Hang 2","My")
hangSanXuat3 = hangSanXuat("Hang 3","Trung Quoc")

boPhim1 = boPhim("Bo Gia",2020,hangSanXuat1.getTenHangSanXuat(),hangSanXuat1.getQuocGia(),65000,ngay1.getNgay,ngay1.getThang(),ngay1.getNam())
boPhim2 = boPhim("Running Man",2021,hangSanXuat2.getTenHangSanXuat(),hangSanXuat2.getQuocGia(),100000,ngay2.getNgay(),ngay2.getThang(),ngay3.getNam())
print("Bo phim 1 co gia ve lon hon bo phim 2: {0}".format(boPhim1.kiemTraGiaVe(boPhim2.getGiaVe())))

print("Ten hang san xuat bo phim 2: {0}".format(boPhim2.getTenHangSanXuat()))

print("Gia ve bo phim 1 sau khi giam 10%: {0} ".format(int(boPhim1.giaSauKhuyenMai(10))))
print("Gia ve bo phim 1 sau khi giam 20%: {0} ".format(int(boPhim1.giaSauKhuyenMai(20))))

# boPhim3 = boPhim("Kham pha Ba Lan", 2025,hangSanXuat3,115000,ngay3)
