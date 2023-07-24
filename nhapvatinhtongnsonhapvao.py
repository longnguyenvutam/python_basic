"""
Bai tap tinh tong n so nhap vao tu ban phim

"""


def tinhTong(listNumber):
    tong = 0
    for x in listNumber:
        tong = tong + x
    return tong

luachon = 'Yes'
list = []
while(luachon == "Yes"):
    n = int(input('Nhap vao cac so can tinh tong: '))
    list.append(n)
    luachon = input('Ban co muon nhap them khong Yes/No: ')

tong = tinhTong(list)

print('Tong cac so nhap vao la: {0}'.format(tong))