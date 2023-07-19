n = -1
while(n<=0):
    n = int(input('Nhap so lon hon 0: '))
print(n)
sodu=0
ketqua=''
while(n>0):
    ketqua = str(n%2)+ketqua
    n = n//2
print('Ket qua: {0}'.format(ketqua))
