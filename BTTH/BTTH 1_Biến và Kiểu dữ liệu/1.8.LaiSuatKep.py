"""
    Nhập số tiền gốc, lãi suất %/năm, số năm
    Tính số tiền sau n năm với công thức: A = P(1 + r)^t
"""
while True:
    P = int(input("Nhap vao so tien goc P = "))
    if P > 0:
        break
    else:
        print("So tien goc phai lon hon 0")

while True:
    r = float(input("Nhap vao lai suat r = "))
    if r > 0:
        break
    else:
        print("So tien goc phai lon hon 0")

while True:
    n = int(input("Nhap vao so nam gui tien n = "))
    if n > 0:
        break
    else:
        print("So nam phai lon hon 0")


def tinh_lai_suat_kep(P, r, n):
    A = round(P * (1 + r/100)**n, 2)
    return A

print("Lai suat kep la", tinh_lai_suat_kep(P, r, n))



# Optimize:

# def nhap_so_duong(thong_bao, kieu_du_lieu=float):
#     """Hàm nhập số dương, tránh lặp code"""
#     while True:
#         try:
#             gia_tri = kieu_du_lieu(input(thong_bao))
#             if gia_tri > 0:
#                 return gia_tri
#             else:
#                 print("Gia tri phai lon hon 0!")
#         except ValueError:
#             print("Vui long nhap so hop le!")
#
# # Sử dụng:
# P = nhap_so_duong("Nhap so tien goc P = ", float)
# r = nhap_so_duong("Nhap lai suat %/nam r = ", float)
# n = nhap_so_duong("Nhap so nam n = ", int)
#
# def tinh_lai_suat_kep(P, r, n):
#     return P * (1 + r/100)**n
#
# print(f"Lai suat kep la: {tinh_lai_suat_kep(P, r, n):,.0f}")