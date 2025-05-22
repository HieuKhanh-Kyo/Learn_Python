# Xd CT quan ly tuyen sinh lop 10 cua truong X:
# So bao danh la mot chuoi co do dai bang 5
# Diem toan va van la mot so thuc co gia tri tu 1 - 10
# Thuc hien cac cong viec sau:
#   + Nhao ds thi sinh tu ban phim
#   + In ds vua nhap ra man hinh
#   + Hien thi danh sach thi sinh co tong diem >10
#   + Hien thi DS thi sinh bi diem liet ra man hinh (co it nhat 1 diem thi 0 diem)

DS_thi_sinh = []
n = int(input("Nhap so luong thi sinh: "))

for i in range(n):
    DS_TS = {"SBD" : "","Toan" : "", "Van" : ""}

    for j in DS_TS:
        print(f"{j} : {DS_TS[j]}")
        values = input()
        DS_TS[j] = values

    DS_thi_sinh.append(DS_TS)

print("DS thi sinh:")
for i in DS_thi_sinh:
    print(f"SBD: {i['SBD']}, Toan: {i['Toan']}, Van: {i['Van']}")

# Hien thi danh sach thi sinh co tong diem >10
DSTS_diem_cao = []
for i in DS_thi_sinh:
    Tong_diem = int(i['Toan']) + int(i['Van'])
    if int(Tong_diem) > 10:
        DSTS_diem_cao.append(i['SBD'])

for i in DSTS_diem_cao:
    print("Nhung thi sinh co tong diem > 10 co SBD la:", i)

# Hien thi DS thi sinh bi diem liet ra man hinh (co it nhat 1 diem thi 0 diem)
DSTS_diem_liet = []
for i in DS_thi_sinh:
    if int(i['Toan']) == 0 or int(i['Van']) == 0:
        DSTS_diem_liet.append(i['SBD'])

for i in DSTS_diem_liet:
    print("Nhung thi sinh bi diem liet co SBD la:", i)