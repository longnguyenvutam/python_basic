"""
Chuong trinh rut tham trung thuong thong qua so dien thoai

Credit: Long Nguyen 
"""

import random
#Khai bao set
thungPhieu = set()
luaChon = 0

while(luaChon != 4):
    print("MENU")
    print('Vui long lua chon chuc nang:')
    print('1 - Them 1 so dien thoai vao thung phieu')
    print('2 - Xoa 1 so dien thoai khoi thung phieu')
    print('3 - Quay so ngau nhien lay ra 1 so dien thoai')
    print('4 - Ket thuc chuong trinh')
    print('5 - In thung phieu hien tai')

    luaChon = int(input('Lua chon: '))

    if(luaChon == 1):
        soDienThoai = input('Nhap vao so dien thoai can them: ')
        thungPhieu.add(soDienThoai)
    
    elif(luaChon == 2):
        soDienThoai == input('Nhap so dien thoai can xoa: ')
        thungPhieu.discard(soDienThoai)
    
    elif(luaChon == 3): 
        vitri = random.randint(0,len(thungPhieu))
        print('So dien thoai trung thuong la: {0}'.format(list(thungPhieu)[vitri]))
        
    elif(luaChon == 5):
         print('Thung phieu hien tai co cac so dien thoai sau: ')
         print(thungPhieu, end=' ')

    elif(luaChon == 4):
         print('Bye bye')
         break;        

    print()