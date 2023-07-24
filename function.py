"""
Hàm là 1 khối mã chỉ chạy khi được gọi
Truyền dữ liệu là tham số
Khai báo hàm: def <tên hàm> (<tham số>):

"""

def xinChao():
    print('Xin chào')

xinChao()


#Argument

def xinChao2(hoVaTen):
    print('Xin chao {0}'.format(hoVaTen))

xinChao2("Nguyen Vu Tam Long")

#Có thể nhận nhiều argument, cach nhau boi dau ,

def xinChao3(ho, chulot,ten):
    print("Xin chao {0} {1} {2}".format(ho,chulot,ten))

xinChao3("Nguyen","Vu Tam","Long")

#Neu khong biet chinh xac co bao nhieu doi so co the them dau * vào trước đối sô
#Các dối sô truyền vào thành dạng tuple

def xinChao4(*Arg):
    print(type(Arg))
    print("Xin chao {0} {1} {2}".format(Arg[0],Arg[1],Arg[2]))

xinChao4("Nguyen","Vu Tam","Long")

def tinhTong(*giaTri):
    sum = 0
    for x in giaTri:
        sum = sum + x
    print(type(sum))
    print(sum)

tinhTong(1,2)
tinhTong(1,5,7,8,9,5)

#Truyen nhieu doi so, xac dinh thong qua  ten, su dun **

def xinChao5(**ten):
    print("Xin chao {0}".format(ten["ho"]))

xinChao5(ho="Nguyen", tenLot="Vu Tam",ten= "Long")

#Su dung tu khoa return de tra ve gia tri

def tinhTich(*giaTri):
    tich = 1
    for x in giaTri:
        tich = tich * x
    return tich

tich = tinhTich(2,5,10)
print(tich)

