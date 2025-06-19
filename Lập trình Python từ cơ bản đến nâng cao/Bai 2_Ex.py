# Chuyen 1 so tu he co so 10 sang he co so 8 dùng print

# a = 10
# print("%o" %(a))

# Hiển thị một số dạng số thực (float) với 2 chữ số sau phần thập phân dùng print

b = 25.85623
print("%.2f" %(b))


# 2.1. Viet chuong trinh tinh gia tri ham so f(x)= e**x - x tai gia tri x = 0.501 va in ket qua ra man hinh

import math
x = 0.501

f = pow(math.e, x) - x
f1 = math.e ** x - x

print(round(f,2), f1)

# 2.2 Viet chuong trinh cho ng dung nhap vao mot so x bat ky sau do tinh va hien thi ra man hinh gia tri x^2, x^3, x^4

y = int(input("So y la "))

print("Gia tri y^2 la", y**2, "\nGia tri y^3 la", y**3, "\nGia tri y^4 la", y**4,)

# 2.3. Viet chuong trinh cho nguoi dung nhap vao mot so thuc la nhiet do f, sau do chuyen sang nhiet do C theo cong thuc

a = float(input("Nhap nhiet do f la "))

b = (a - 32)/ 1.8

print("Nhiet do C la", round(b,2), "C")

# 2.4. Viet CT nhan vao gia tri chuoi, lay 2 ky tu dau và cuoi cua chuoi do. Neu chuoi <2, tra ve chuoi rong (empty)

s = input("Enter a string: ")
res = ""

if len(s) < 2:
    res = ""
else:
    res = s[0 : 2] + s[-2:]

# print(res)

# 2.5. Viet CT thuc hien doi cho 2 so

# m = "Gia tri cua so thu nhat la 34"
# n = "Gia tri cua so thu hai la 56"
#
# print(m.replace("34", n[-2:]),
#       n.replace("56", m[-2:]))

m = 39
n = 25

# tg = m
# m = n
# n = tg

m, n = n, m

print(m, n)

# Nhap vao mot chuoi sdt gom 10 so, ma hoa chuoi dt nay bang cach thay 3 so cuoi bang dau *

d = input("Nhap so dien thoai cua ban: ")
res = ""

if len(d) != 10:
    res = "Hay nhap du 10 so!!"
else:
    res = d.replace(d[-3:],"***")

print(res)
