# Viet CT tinh s = x^2 + x^4 + ... + x^2n

# import math
# n = int(input("Enter n= "))
# x = int(input("Enter x= "))
# s = 0
#
# for i in range(2,(2*n)+1,2):
#     s += math.pow(x,i)
# print(s)

# 10.000.000 gui ngan hang, lai suat 1%/thang, tinh so tien nhan duoc sau 5 nam

# x = 10000000
#
# for i in range( 5*12 ):
#     x += (x * 0.01)
# print(round(x))

# Nhap vao 2 so nguyen, tra ra uoc chung lon nhat cua 2 so do

# import math
# print(math.gcd(12,18))

a = int(input("a = "))
b = int(input("b = "))

# if a > b:
#     a, b = b, a

# for i in range(a , 0, -1):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break
#

# while b != 0:
#     a, b = b, a % b  # Áp dụng thuật toán Euclid
#
# print(a)  # 'a' sẽ là UCLN

# Dung phep toan tru

# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# print(a)

# Dung phep toan nhan

while a * b != 0:
    if a > b:
        a %= b
    else:
        b %= a
print(a + b)