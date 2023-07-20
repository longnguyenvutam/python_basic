"""
Chuong trinh tinh tong day so
N la do dai cua day so
M la so chu can tinh tong

quy luat day so: 1,N,2,N-1,3,N-2,4,N-3,...
vi du: N = 6
1,6,2,5,3,4,4,3,5,2,6,1
M = 3
--> tong cua 1 + 6 + 2 = 9

"""

n = 0
m = 0
daySo = []
import math
while(n < 1 or n > pow(10,9)):
    n = int(input('Nhap so N: '))

while(m < 1 or m > pow(10,9)):
    m = int(input('Nhap so M la so chu so can tinh tong: '))

for i in range(0,n):
    if (i==0):
        daySo.insert(0,1)
    elif (i==1):
        daySo.insert(1,n)
    elif (i==2):
        daySo.insert(i,i)
    elif(i%2==0):
        daySo.insert(i,i-1)
    else:
        daySo.insert(i,daySo[i-2] - 1)

for i in range(n):
    print(daySo[i],end=' ')

print()
tong = 0
for i in range(m):
    tong = tong + daySo[i]

print('Tong {0} chu so trong day so la: {1}'.format(m,tong)) 
