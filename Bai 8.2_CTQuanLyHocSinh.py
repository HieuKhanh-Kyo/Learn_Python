# Viet Ct quan ly hoc sinh thuc hien cac hoat dong sau:
# 1. Nhap DS hoc sinh gom cac thong tin: Ma HS, Ten HS, Diem Toan, Diem Van
# 2. Tinh Diem trung binh: (Diem Toan + Diem Van)/2
# 3. Xep loai HS theo diem trung binh theo dieu kien:
#   - DTB > 9            -> Xuat sac
#   - 8 <= DTB < 9       -> Gioi
#   - 7 <= DTB < 8       -> Kha
#   - 5 <= DTB < 7       -> Trung Binh
#   - DTB < 5            -> Yeu
# 4. In thong tin cua cac HS ra man hinh


def nhap_dshs():
    # Nhap MaHS
    while True:
        MaHS = input("Nhap ma HS:")
        if len(MaHS.split()) > 0:
            break

    # Nhap TenHS
    while True:
        TenHS = input("Nhap ten HS:")
        if len(TenHS.split()) > 0:
            break

    # Nhap Diem Toan
    while True:
        Diem_Toan = float(("Nhap diem Toan:"))
        if 0 <= Diem_Toan <= 10:
            break

    # Nhap Diem Van
    while True:
        Diem_Van = float(("Nhap diem Van:"))
        if 0 <= Diem_Van <= 10:
            break

    return {MaHS, TenHS, Diem_Toan, Diem_Van}

