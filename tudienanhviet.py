
tudien = dict()
luaChon = 1

while True:
    print("------MENU------")
    print("1 - Them tu vung moi")
    print("2 - Tra cuu y nghia cua 1 tu vung")
    print("3 - Cap nhat y nghia cua tu vung")
    print("4 - Xoa di 1 tu vung trong tu dien")
    print("5 - Xoa toan bo tu vung")
    print("6 - In toan bo tu dien")
    print("7 - Ket thuc chuong trinh")

    try:
        luaChon = int(input('Nhap cac lua chon tu 1-7: '))
    except:
        print('Vui long nhap cac lua chon tu 1-7')
        continue

    if(luaChon == 1):
        key = input('Nhap tu vung: ')
        value = input('Nhap y nghia cua tu vung {0}: '.format(key))
        tudien.update({key:value})

    elif(luaChon == 2):
        timthay = 0
        key = input('Nhap tu vung can tra cuu: ')
        for x in tudien.keys():
            if(x == key):
                print('Nghia cua tu {0} la {1}'.format(key,tudien[key]))
                timthay = 1
        if timthay == 0:
            print("Tu ban nhap khong co trong tu dien")

    elif(luaChon == 3):
        timthay  = 0
        key = input('Nhap tu vung can cap nhat y nghia: ')
        for x in tudien.keys():
            if(x == key):
                value = input('Nhap y nghia: ')
                tudien.update({key:value})
                timthay = 1
        if(timthay == 1):
            print('Cap nhat y nghia tu {0} thanh cong'.format(key))
        else:
            print('Tu ban nhap khong co trong tu dien')
            
    elif(luaChon == 4):
        key = input('Nhap tu vung can xoa: ')
        timthay = 0
        for x in list(tudien.keys()):
            if(x == key):
                tudien.pop(key)
                timthay = 1
        if (timthay == 0):
            print('Tu ban nhap khong co trong tu dien')
        else:
            print('Da xoa tu vung {0} ra khoi tu dien'.format(key))

    elif(luaChon == 5):
        tudien.clear()
        print('Xoa toan bo tu dien')

    elif(luaChon == 6):
        for key,value in tudien.items():
            print("Tu vung {0} co nghia la {1}".format(key,value))

    elif(luaChon == 7):
        print("Bye Bye")
        break;
    
    else:
        print('Not a valid option')

    print()
                         
 