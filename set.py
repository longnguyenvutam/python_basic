#Set la tap hop khong co thu tu, khong the thay doi vaf khong duoc lap chi muc.
#Cac muc Set la khogn the thay doi, nhung co the xoa cac muc va them cac muc moi
#Su dung { } de khai bao Set

monHoc = {'Toan', "Ly", "Hoa"}
print(monHoc)

#Duyet cac phan tu trong Set
for i in monHoc:
    print(i,end='\t')

print()
#Them phan tu vao Set
monHoc.add('Lich Su')
print(monHoc)

#Cap nhat them phan tu tu 1 set khac
hocThem = {'Anh Van', 'Piano'}
monHoc.update(hocThem)
print(monHoc)

#Them List vao Set
hocPhuDao = ['Vo thuat','Mua']
monHoc.update(hocPhuDao)
print(monHoc)

#Xoa phan tu khoi Set
#Dung phuong thuc remove 
#monHoc.remove('Sinh hoc') --> Sinh hoc khong ton tai se bao loi
monHoc.remove('Vo thuat')

#Dung phuong thuc discard tot hon remove

monHoc.discard('Sinh hoc') #khong bao loi neu khong ton tai trong Set
monHoc.discard('Toan')

monHoc.pop() #Xoa phan tu dau tien
monHoc.clear() #Xoa toan bo phan tu trong Set

