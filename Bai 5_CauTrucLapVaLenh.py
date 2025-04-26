# Cau truc lap FOR:
#   for <ten_bien> in <tap_hop>
#       <lenh_trong_for>

# s = "Hello"
# for i in s:
#     print(i)

# for i in range(1, 10, 1):  #Neu i >= end -> thi se dung vong lap
#     print(i)


# Tinh tong s = 1 + 2 + 3 + 4 +.... + n voi n nhap tu ban phim

# n = int(input("Enter n = "))
# s = 0
#
# for i in range(1, n + 1):
#     s += i  # s = s + i
#
# print(s)  # sau khi thuc hien vong for, cap nhat va in ra gia tri cuoi cung cua s

# i = 1 -> s = 0 + 1 = 1
# i = 2 -> s = 1 + 2 = 3
# i = 3 -> s = 3 + 3 = 6
# i = 4 -> s = 6 + 4 = 10
# i = 5 -> s = 10 + 5 = 15

# a = [0,1,4,2,5,3,4,5,6,3,2,2,3,5,6,6,7,8,8,5,4,2342,33,3,22,3,42,4,2,24,34,2,342,423,42,34]
# s = 0
# for i in a:
#     if i % 2 == 0:
#         s = s + i
# print(s)

# s = 0
# for i in range(0, len(a)):
#     if a[i] % 2 == 0:  # a tro theo index, i=0 -> a[0] = 0, a[5] = 3
#         s += a[i]
# print(s)

#Cau truc lap WHILE
# i = 2
# while (i <= 11):
#     print(i)
#     i += 1

# Tinh n! voi n nhap tu ban phim

# n = int(input("Enter n = "))
# i = 1
# s = 1
# while (i <= n):
#     s = s * i
#     i +=1
# print(s)

# for i in range(5):
#     i  += 1
#     print(i + 1)

# Cau lenh BREAK
# i = 6
# while i <= 10:
#     if i <= 5:
#         break
#     print("Ca hanh")
#     i = i + 1

# Nhap vao cac so duong va tinh tong cac so duong vua nhap
# Neu gap so am thi thoat va in ra tong cac so duong vua nhap vao

# s = 0
# while True:
#     n = int(input("Enter n = "))
#     if n < 0:
#         break
#     s += n
# print(s)

# Cau lenh CONTINUE

# i = 1
# while i <= 10:
#     i += 1
#     print("Cu hanh")
#     continue
#     print("Ca Hanh")

# Tinh tong cac so chan tu 1 den n voi n nhap tu ban phim

n = int(input("Enter n = "))
s = 0

for i in range(1,n+1):
    if i % 2 == 1:
        continue   # neu i khong chia het cho 2 thi bo qua so do, tiếp tuc duyet phan tu tiep
    s += i
print(s)
