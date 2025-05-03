# Xay dung CT quan ly hang hoa voi cac cong viec:
#   Nhap tt cac mat hang hien co tai cua hang gom: Ten hh, So luong, Gia ban
#   Tinh tong so luong hh cua cua hang
#   Hien thi thong tin cac mat hang co so luong <10
#   Hien thi thong tin cac mat hang co so luong >60

DS_hang_hoa = []
n = int(input("Nhap so luong mat hang: "))

for i in range(n):
    DS_hh = {"Ten mat hang " : "", "So luong " : "", "Gia ban " : ""}

    for j in DS_hh:
        print(f"{j} : {DS_hh[j]}")
        values = input()
        DS_hh[j] = values

    DS_hang_hoa.append(DS_hh)

print(DS_hang_hoa)

# Tinh tong so luong hh cua cua hang
tong_so_luong_hh = 0
for i in range(n):
    tong_so_luong_hh += int(DS_hang_hoa[i]["So luong "])
print(tong_so_luong_hh)

# Hien thi thong tin cac mat hang co so luong <10
HH_so_luong_it = []
for i in DS_hang_hoa:
    if int(i["So luong "]) < 10:
        HH_so_luong_it.append(i)

print("Cac mat hang co so luong < 10 la ", HH_so_luong_it)

# Hien thi thong tin cac mat hang co so luong > 60
HH_so_luong_nhieu = []
for i in DS_hang_hoa:
    if int(i["So luong "]) > 60:
        HH_so_luong_it.append(i)

print("Cac mat hang co so luong > 60 la ", HH_so_luong_nhieu)

#Lay ra "ten" cua cac mat hang co so luong <10
# Ten_mat_hang_so_luong_it = []
#
# for item in DS_hang_hoa:
#     if int(item["So luong "]) < 10:
#         Ten_mat_hang_so_luong_it.append(item["Ten mat hang "])
#
# print("Ten mat hang co so luong < 10 la:", Ten_mat_hang_so_luong_it)