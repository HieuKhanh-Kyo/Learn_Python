#khai bao va khoi tao list

# a = [1, 4.5, "Hello World"]
#
# b = list(["ca hanh", 7.10])
#
# c = [[1,3], 7, "ca hanh", [2,0,0,3]]


# print  <ten_danh_sach>[start: end: step]

# d = [1, 2, 3, 4, 5, 6, 7]
# print(d[0: 8: 2])

# <ten_list>.append() : them phan tu vao sau cung trong list

# <ten_list>.insert(vi_tri_them, gia_tri_them):  them phan tu nao vao vi tri nao

# <ten_list>.__delitem__(<index/ vi_tri_can_xoa>):  xoa mot phan tu trong list

# <ten_list>.remove(<gia_tri_can_xoa):  xoa mot gia tri trong list


# Nhap vao mot danh sach tu ban phim

# a = []   # khoi tao 1 list rong
#
# n = int(input("n = "))   # gioi han so luong phan tu trong list
#
# for i in range(n):
#     x = int(input())    # nhap vao cac phan tu de dua vao list
#     a.append(x)         # moi lan lap se them x vao sau list

# for i in a:    # duyet qua tat ca cac gia tri trong mang, i nhan tung gia tri trong mang a
#     print("Gia tri phan tu cua mang", i)   # moi lan duyet in ra 1 gia tri trong mang

# for i in range(n):
#     print("Phan tu thu", i +1, a[i])


# Nhap vao n phan tu cua list va tinh tong cac phan tu vua nhap

# tong = sum(a)
# # sum(<list>):   tinh tong các phan tu trong mang
# print(tong)

# len(<list>):   dem so luong phan tu trong danh sach

# sorted(<list>):   sap xep cac phan tu cua mang theo thu tu tang dan
# sorted(<list>, reverse = True ):   sap xep theo chieu nguoc lai/ giam dan

b = [4,5,9,8,1,7]
c = sorted(b, reverse=True)
print(c)

# max(<list>):  tra ra GTLN cua list
# min(<list>):  tra ra GTNN cua list