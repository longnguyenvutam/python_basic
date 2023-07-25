class conNguoi:

    def __init__(self,hoVaTenConNguoi,namSinhConNguoi):
        self.hoVaTen = hoVaTenConNguoi
        self.namSinh = namSinhConNguoi

    def getHoVaTen(self):
        print('Ho va Ten la: {0}'.format(self.hoVaTen))

    def setHoVaTen(self,newHoVaTen):
        self.hoVaTen = newHoVaTen

    def getNamSinh(self):
        print("Nam sinh cua {0} la {1} ".format(self.hoVaTen,self.namSinh))
    
    def setNamSinh(self,newNamSinh):
        self.namSinh = newNamSinh

    def an(self):
        print("{0} dang mam mam".format(self.hoVaTen))

    def uong(self):
        print("{0} dang uc uc".format(self.hoVaTen))

    def ngu(self):
        print("{0} dang kho kho".format(self.hoVaTen))


class hocSinh(conNguoi):

    def __init__(self,hoVaTen,namSinh,tenLop,tenTruong):
        conNguoi.__init__(self,hoVaTen,namSinh)
        self.tenLop = tenLop
        self.tenTruong = tenTruong

    def getTenLop(self):
        print("{0} hoc lop {1}".format(self.hoVaTen,self.tenLop))

    def setTenLop(self,newTenLop):
        self.tenLop = newTenLop

    def getTenTruong(self):
        print("{0} dang hoc truong {1}".format(self.hoVaTen,self.tenTruong))

    def setTenTruong(self,newTenTruong):
        self.tenTruong = newTenTruong

    def lamBaiTap(self):
        print("{0} dang lam bai tap".format(self.hoVaTen))   


conNguoi1 = conNguoi("Nguyen Vu Tam Long","1992")
conNguoi1.getHoVaTen()
conNguoi1.getNamSinh()

conNguoi2 = hocSinh("Nguyen Van A","2002","A1","Ha Long")
conNguoi2.getHoVaTen()
conNguoi2.getNamSinh()
conNguoi2.getTenLop()
conNguoi2.getTenTruong()
conNguoi2.an()
conNguoi2.ngu()
conNguoi2.uong()
conNguoi2.lamBaiTap()
conNguoi2.setHoVaTen("Nguyen Van B")
conNguoi2.getHoVaTen()
