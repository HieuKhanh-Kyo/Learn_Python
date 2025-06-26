"""
    Nhập email, kiểm tra có chứa "@" và "." không
    -> output: "Email hợp lệ" hoặc "Email không hợp lệ"

    TC:  test@gmail.com  -> hợp lệ
         testgmail.com   -> không hợp lệ
"""

while True:
    email = input("Nhap email: ")
    if "@" in email and "." in email:
        print("Email hợp lệ!")
        break
    else:
        print("Email không hợp lệ!")


# while True:
#     email = input("Nhap email: ")
#     if email.endswith("@gmail.com") and len(email) > 10:
#         print("Email hợp lệ!")
#         break
#     else:
#         print("Email không hợp lệ!")
