"""
Chuong trinh tim uoc so cua so nguyen duong n

"""

n = -1
uocso = []
tong = 0
while (n<0):
    n = int(input('Nhap so nguyen duong n > 0: '))

for i in range(1,n+1):
    if(n % i == 0):
        uocso.append(i)
print('Cac uoc so cua so nguyen duong {0} la: '.format(n))
for i in range(len(uocso)):
    print(uocso[i],end=' ')

#Tinh tong cac uoc so 
print()
for i in range(len(uocso)):
    tong = tong + uocso[i]

print('Tong cac uoc so cua so nguyen duong {0} la {1}'.format(n,tong))

tich = 1
#Tinh tich cac uoc so
for i in range(len(uocso)):
    tich = tich * uocso[i]

print('Tich cac uoc so cua so nguyen duong {0} la {1}'.format(n,tich))

#Dem so luong cac uoc so
print('So luong cac uoc so cua so nguyen duong {0} la {1}'.format(n,len(uocso)))

#Liet ke cac uoc so le
uocsole = []
for i in range(len(uocso)):
    if(uocso[i] % 2 != 0):
        uocsole.append(uocso[i])

print('Cac uoc so le cua {0} la: '.format(n))
for i in range(len(uocsole)):
    print(uocsole[i], end = ' ')

print()

#Tinh tong cac uoc so chan 
uocsochan = []
for i in range(len(uocso)):
    if(uocso[i] % 2 == 0):
        uocsochan.append(uocso[i])

tongsochan = 0
for i in range(len(uocsochan)):
    tongsochan = tongsochan + uocsochan[i]

print('Tong cac uoc so chan cua {0} la: {1}'.format(n,tongsochan))

#Tim uoc le lon nhat
solelonnhat = max(uocsole)
print('Uoc so le lon nhat cua {0} la {1}'.format(n,solelonnhat))

