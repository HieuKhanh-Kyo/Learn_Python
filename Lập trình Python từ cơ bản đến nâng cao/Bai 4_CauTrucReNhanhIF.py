#Xep loai hoc sinh
# dtb < 5 -> Yeu
# 5 <= dtb < 7 -> TB
# 7 <= dtb < 8 -> Kha
# 8 <= dtb < 9 -> Gioi
# >= 9 -> Xuat sac

dtb = float(input("Nhap vao diem trung binh "))

if dtb >= 0 and dtb <= 10:
    if dtb <5:
        print("Yeu")
    elif 5<=dtb<7:
        print("TB")
    elif 7<=dtb<8:
        print("Kha")
    elif 8<=dtb<9:
        print("Gioi")
    else:
        print("Xuat sac")
else:
    print("Ban vui long nhap diem trong khoang tu 0 den 10")