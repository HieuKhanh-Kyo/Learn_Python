# Viet CT nhap vao 2 da thuc mot bien sau do tinh tong cua 2 da thuc, tinh gia tri cua tung da thuc tai x bat ky nhap tu ban phim

def nhapDaThuc():
    daThuc = {}

    while True:
        mu = int(input("Nhap mu = "))
        if mu == -1 :
            break

        heSo = float(input("Nhap He So = "))
        if heSo != 0:
            daThuc[mu] = heSo

    return daThuc


# def hienThiDaThuc(daThuc):
#     chuoiDaThuc = ""
#     for mu in sorted(daThuc.keys()):
