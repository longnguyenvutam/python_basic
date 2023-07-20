
import math
soTuNhien = [1,3]
viTriCanTim = 0
while(viTriCanTim <= 0):
    viTriCanTim = int(input('Nhap vi tri can tim > 0: '))

timThay = 0
#1 3 6 8 11 13 16 18 21 23 26 28 31 33 36 38 41 43 46

#Vi tri chan + 5
#Vi tri le + 5
for i in range(2,1000000):
    if (viTriCanTim == 1):
        print(f'Vi tri {viTriCanTim} la so 1')
        timThay = 1
        break;
    if (viTriCanTim == 2):
        print(f'Vi tri {viTriCanTim} la so 3')
        timThay = 1
        break;
    if (i % 2 == 0):
        a = soTuNhien[i-2] + 5
        soTuNhien.insert(i,a) 
    else:
        soTuNhien.insert(i,soTuNhien[i-2] + 5)

if(timThay == 0):
    print('Vi tri {0} la so {1}'.format(viTriCanTim,soTuNhien[viTriCanTim-1]))

# for i in range(len(soTuNhien)):
#     print(soTuNhien[i],end=" ")      