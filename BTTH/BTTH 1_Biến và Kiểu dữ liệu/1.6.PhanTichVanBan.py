"""
    Nhập vào một câu văn bản
    -> Đếm số ký tự (không kể space), số từ, số nguyên âm

    TC: "Hello World"   -> Ký tự: 10, Số từ: 2, Nguyên âm: 3
"""

Van_Ban = input("Nhap vao mot cau van ban: ")

ky_tu = len(Van_Ban.replace(" ", ""))
so_tu = len(Van_Ban.split())

list_nguyen_am = "aeiouAEIOU"
nguyen_am = 0
for i in Van_Ban:
    if i in list_nguyen_am:
        nguyen_am += 1

print(f"{Van_Ban} co ky tu: {ky_tu}, so tu: {so_tu}, nguyen am: {nguyen_am}")