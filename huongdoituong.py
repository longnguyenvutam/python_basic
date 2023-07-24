"""
Class:
Khai bao class:


"""
class SimpleClass:
    i = 3

    def __init__(self):
        self.j = 7

    #method

    def printMe(self):
        print(self.j)

#Create new object

objectA = SimpleClass()
objectB = SimpleClass()

objectA.printMe()
print(objectB.i)

#Thay doi gia tri cua thuoc tinh

objectA.i = 100
print(objectA.i)

class SimpleClass2:
    #constructor

    def __init__(self) -> None:
        self.name = "Long"

    def xinChao(self,name):
        print("Xin chao {0}".format(name))

    #static method
    @staticmethod
    def hi(name):
        print('Hi {0}'.format(name))

    @staticmethod
    def hello(name):
        print("Hello {0}".format(name))   

objectC = SimpleClass2()
objectD = SimpleClass2()

objectC.hi("Long")
objectC.hello("Truc")
objectC.xinChao("Bong")


class Date:

    def __init__(self,giaTriNgay,giaTriThang,giaTriNam):
        self.ngay = giaTriNgay
        self.thang = giaTriThang
        self.nam = giaTriNam

    def ngayBaoNhieuTrongNam(self):
        giaTriNgayTrongNam = 0
        tongSoNgay = 0
        if self.thang == 1:
            return self.ngay
        else:
            for x in range(1,self.thang):
                giaTriNgayTrongNam += self.thangCoBaoNhieuNgay(x,self.nam)
        tongSoNgay = giaTriNgayTrongNam + self.ngay
        return tongSoNgay
    
    # @staticmethod
    # def ngayBaoNhieuTrongNam(month,year):
    #     if month == 1:
    #         return 31
    #     else:
    #         for x in range(1,month):
    #             giaTriNgayTrongNam += thangCoBaoNhieuNgay(x,year)
    #     return giaTriNgayTrongNam

    @staticmethod
    def thangCoBaoNhieuNgay(thang,nam):
        if thang==1:
            soNgay = 31
        elif thang==3:
            soNgay = 31
        elif thang==4:
            soNgay = 30
        elif thang==5:
            soNgay = 31
        elif thang==6:
            soNgay =30
        elif thang==7:
            soNgay = 31
        elif thang==8:
            soNgay = 31
        elif thang==9:
            soNgay = 30
        elif thang==10:
            soNgay = 31
        elif thang==11:
            soNgay = 30
        else:
            soNgay = 31

        if thang == 2:
            if ((nam % 400 == 0) or (nam % 4 == 0 and  nam % 100 !=0 ) == 29):
                soNgay = 29
            else:
                soNgay = 28
        return soNgay


# ngayA = Date
# m = int(input('Nhap thang: '))
# y = int(input('Nhap nam: '))
# print('So ngay trong cua thang {0} la {1}'.format(m,ngayA.thangCoBaoNhieuNgay(m,y)))

ngayA = Date(15,3,2022)
print(ngayA.ngayBaoNhieuTrongNam())

ngayB = Date(15,1,2022)
print(ngayB.ngayBaoNhieuTrongNam())



    