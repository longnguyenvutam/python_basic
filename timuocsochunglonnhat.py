"""
Bai tap tim uoc so chung lon nhat cua 2 so
Tim uoc so chung lon nhat cua 2 so = cach tim uoc so cua tung so
Sau do so sanh cac uoc so cua so thu nhat va thu hai de tim ra uoc so chung lon nhat

"""


def timUocSoChungLonNhat(*arg):
    uocChungLonNhat = 1
    # for i in range(len(arg[0])):
    #     print (arg[0][i], end = ' ')
    # print()
    # for i in range(len(arg[1])):
    #     print (arg[1][i],end = ' ')
    for i in range(len(arg[0])):
        for y in range(len(arg[1])):
            if (arg[1][y] == arg[0][i]):
                uocChungLonNhat = arg[0][i];
                break;
    print()
    return uocChungLonNhat


def timUocSo(a):
    uocSo = []
    for i in range(1,a+1):
        if(a % i == 0):
            uocSo.append(i);
    return uocSo
a = 0
b = 0
while (a<=0):
    a = int(input("Nhap so thu nhat: "))

while (b<=0):
    b = int(input("Nhap so thu hai: "))

uocSoCuaSoThuNhat = []
uocSoCuaSoThuHai = []
uocSoCuaSoThuNhat = timUocSo(a)
uocSoCuaSoThuHai = timUocSo(b)

print("List cac uoc so cua so thu nhat: {0}".format(uocSoCuaSoThuNhat))
print("List cac uoc so cua so thu nhat: {0}".format(uocSoCuaSoThuHai))

UocSoChungLonNhat = timUocSoChungLonNhat(uocSoCuaSoThuNhat,uocSoCuaSoThuHai)
print("Uoc so chung lon nhat cua 2 so {0} va {1} la {2}".format(a,b,UocSoChungLonNhat))