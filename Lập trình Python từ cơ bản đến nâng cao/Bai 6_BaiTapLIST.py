# Viet CT trao doi phan tu dau voi phan tu cuoi trong list, phan tu thu 2 voi phan tu thu n-1 (gia su co n phan tu)

# a = [4,2,6,7,9,8]
# n = len(a)
#
# for i in range(n // 2):
#     gt = a[i]
#     a[i] = a[n - 1 - i]
#     a[n - 1 - i] = gt
#
# print(a)


# Tinh gia tri cua da thuc:  P = a0 + a1x + a2x^2 + ... + anx^n

# a = []
# n = int(input("n = "))
# x = int(input("x = "))
#
# for i in range(n):
#    print("Nhap vao phan tu thu ", i+1, ":", end="")
#    b = int(input())
#    a.append(b)
#
# P = 0
#
# for i in range(n):
#     P += a[i] * x**i
#
# print(P)


#Hang thoi trang co n cua hang tren toan quoc, CT nhap vao cac doanh so cua cac cua hang do:
#   - Sap xep doanh so ban hang tu be den lon
#   - Tinh trung binh doanh so cua n cua hang
#   - Hien thi doanh so ban hang nho nhat, lon nhat

a = []
n = int(input("n = "))
print("Hang thoi trang co ", n, "cua hang")

for i in range(n):
    print("Doanh thu cua cua hang ", i+1, "la ", end="")
    s = int(input())
    a.append(s)
print("Doanh so cua hang tu be den lon la", sorted(a))

# b = 0
# for i in range(n):
#     b += a[i]
# print("Trung binh doanh so cua ", n, "cua hang la", b / n)

b = sum(a)
print("Trung binh doanh so cua", n, "cua hang la", b/n )

print("Doanh so nho nhat la cua hang", a.index(min(a)) + 1, "voi doanh so la", min(a))
print("Doanh so lon nhat la cua hang", a.index(max(a)) + 1, "voi doanh so la", max(a))