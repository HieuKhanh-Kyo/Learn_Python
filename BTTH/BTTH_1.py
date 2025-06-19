# nhap vao 1 so nguyen n, kiem tra so do co phai so nguyen to khong
# neu la so nguyen to thi in ra 1
# nguoc lai in ra 0

n = int(input("Enter n ="))

# n = int(input("Enter n ="))
# hanh = True
#
# for i in range(2,n):
#     if n % i == 0:
#         hanh = False
#         break
# if hanh:
#     print(1)
# else:
#     print(0)


# nhap vao 1 so nguyen n, kiem tra so do co phai so dep khong
# neu la so dep thi in ra 1
# nguoc lai in ra 0

# n = int(input("Enter n = "))
# s = 0
#
# while n > 0:
#     s += (n % 10)
#     n = n / 10
#
# if s % 10 == 9:
#     print(1)
# else:
#     print(0)


# nhap vao mot so nguyen: tinh tong cac chu so o vi tri chan va tong cac chu so o vi tri le

c = 0
l = 0

for i in range(0, len(str(n)), 2):
    c += int(str(n)[i])

for i in range(1, len(str(n)), 2):
    l += int(str(n)[i])

print ("Tong cac chu so o vi tri chan la ", c)
print ("Tong cac chu so o vi tri le la ", l)



# n = abs(int(input("Enter n =")))  # Lấy giá trị tuyệt đối nếu n âm
# c = 0  # Tổng chữ số ở vị trí chẵn
# l = 0  # Tổng chữ số ở vị trí lẻ
#
# n_str = str(n)  # Chuyển n thành chuỗi để duyệt qua từng ký tự
# for i in range(len(n_str)):
#     if i % 2 == 0:  # Vị trí chẵn (index 0, 2, 4, ...)
#         c += int(n_str[i])
#     else:  # Vị trí lẻ (index 1, 3, 5, ...)
#         l += int(n_str[i])
#
# print("Tổng các chữ số ở vị trí chẵn (index 0, 2, 4, ...):", c)
# print("Tổng các chữ số ở vị trí lẻ (index 1, 3, 5, ...):", l)


# i = 0  # Khởi tạo index ban đầu
#
# while i < len(n_str):  # Điều kiện: index i không vượt quá độ dài chuỗi
