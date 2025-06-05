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


def nhap_tths():
    # Nhap MaHS
    while True:
        MaHS = input("Nhap ma HS: ")
        if len(MaHS.split()) > 0:
            break

    # Nhap TenHS
    while True:
        TenHS = input("Nhap ten HS: ")
        if len(TenHS.split()) > 0:
            break

    # Nhap Diem Toan
    while True:
        Diem_Toan = float(input("Nhap diem Toan: "))
        if 0 <= Diem_Toan <= 10:
            break

    # Nhap Diem Van
    while True:
        Diem_Van = float(input("Nhap diem Van: "))
        if 0 <= Diem_Van <= 10:
            break

    return {"MaHS" : MaHS,"TenHS" : TenHS, "Diem Toan" : Diem_Toan, "Diem Van" : Diem_Van}


def Nhap_DSHS():
    dsHS = []
    while True:
        n = int(input("Nhap so luong HS: "))
        if n > 0:
            break

    for i in range(1, n+1):
        print("Nhap vao thong tin cua HS ", i)
        dsHS.append(nhap_tths())

    return dsHS


def Diem_tb(Diem_Toan, Diem_Van):
    return (Diem_Toan + Diem_Van)/2


def Xep_Loai_HS(Diem_tb):
    xl = ""
    if 9 <= Diem_tb <= 10:
        xl = "Xuat sac"
    elif 8 <= Diem_tb < 9:
        xl = "Gioi"
    elif 7 <= Diem_tb < 8:
        xl = "Kha"
    elif 5 <= Diem_tb < 7:
        xl = "Trung binh"
    else:
        xl = "Yeu"
    return xl


def in_TTHS(dsHS):
    for i in range(len(dsHS)):
        print("Thong tin cua HS ",i + 1)
        print("Ma HS la ", dsHS[i]["MaHS"])
        print("Ten HS la ", dsHS[i]["TenHS"])
        print("Diem Toan la", dsHS[i]["Diem Toan"])
        print("Diem Van la ", dsHS[i]["Diem Van"])
        dtb = Diem_tb(dsHS[i]["Diem Toan"], dsHS[i]["Diem Van"])
        print("HS xep loai: ", Xep_Loai_HS(dtb))


def main():
    dsHS = Nhap_DSHS()
    in_TTHS(dsHS)


main()


