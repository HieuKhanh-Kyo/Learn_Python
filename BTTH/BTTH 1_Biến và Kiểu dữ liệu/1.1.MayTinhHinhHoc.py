"""
    Viết chương trình nhập chiều dài, chiều rộng từ bàn phím
    -> Tính và in ra diện tích, chu vi hình chữ nhật
"""

while True:
    dai = float(input("Nhap chieu dai = "))
    if dai > 0:
        break

while True:
    rong = float(input("Nhap chieu rong = "))
    if rong > 0:
        break

DienTich = dai * rong
ChuVi = (dai + rong) * 2

print(f"Hinh chu nhat co chieu dai = {dai}, rong = {rong} co dien tich = {DienTich} , va chu vi =  {ChuVi}" )


# while True:
#     try:
#         dai = float(input("Nhap chieu dai = "))
#         if dai > 0:
#             print("Chieu dai la", dai)
#             break
#         else:
#             print("Hay nhap so duong")
#     except ValueError:
#         print("Hay thu lai!!!")
