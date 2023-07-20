"""
Chuong trinh ve tam giac *

"""
import time

for hang in range(7):
    for cot in range(7):
        if(hang==1 and 3<cot<5):
            print("*",end=" ")
        elif(hang==2 and 3<cot<6):
            print("*",end=" ")
        elif (hang<3 and cot == 3 ) :
            print('*',end=" ")
        elif(hang==3):
            print('*',end=" ")
        elif(hang==4 and cot < 3):
            print("*",end=" ")
        elif(hang==5 and cot < 2):
            print("*",end=" ")
        elif(hang==6 and cot < 1):
            print("*",end=" ")
        else:
            print(' ',end=" ")  
    print()        

time.sleep(1)

for hang in range(7):
    for cot in range(7):
        if(hang==1 and cot == 4):
            print("*",end=" ")
        elif(hang==2 and cot==5):
            print("*",end=" ")
        elif(hang<3 and cot == 3):
            print("*",end=" ")
        elif(hang==3):
            print("*",end=" ")
        elif(hang==4 and (cot == 0 or cot ==2 )):
             print("*",end=" ")
        elif(hang==5 and cot <2 ):
            print("*",end=" ")
        elif(hang==6 and cot <1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

time.sleep(1)

for hang in range(7):
    for cot in range(7):
        if(cot == 3):
            print("*",end=" ")
        elif(hang==0 and cot>3):
            print("*",end=" ")
        elif(hang==1 and 3<cot<6 ):
            print("*",end=" ")
        elif(hang==2 and cot==4):
            print("*",end=" ")
        elif(hang==4 and 1<cot<3):
            print("*",end=" ")
        elif(hang==5 and 0<cot<3):
            print("*",end=" ")
        elif(hang==6 and cot<3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

time.sleep(1)
print()
for hang in range(7):
    for cot in range(7):
        if(cot == 3):
            print("*",end=" ")
        elif(hang==0 and cot>3):
            print("*",end=" ")
        elif(hang==1 and cot == 5 ):
            print("*",end=" ")
        elif(hang==2 and cot==4):
            print("*",end=" ")
        elif(hang==4 and 1<cot<3):
            print("*",end=" ")
        elif(hang==5 and cot == 1):
            print("*",end=" ")
        elif(hang==6 and cot<3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        