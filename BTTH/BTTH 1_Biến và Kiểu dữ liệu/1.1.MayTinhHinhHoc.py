'''
Viết chương trình nhập chiều dài, chiều rộng từ bàn phím
-> Tính và in ra diện tích, chu vi hình chữ nhật

'''

dai = int(input("Nhap chieu dai = "))
rong = int(input("Nhap chieu rong = "))

DienTich = dai * rong
ChuVi = (dai + rong) * 2

print(f"Hinh chu nhat co chieu dai = {dai}, rong = {rong}, \nco dien tich = {DienTich} , va chu vi =  {ChuVi}" )
