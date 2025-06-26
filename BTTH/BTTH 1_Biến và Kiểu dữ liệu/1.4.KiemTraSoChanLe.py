"""
    Nhập một số nguyên
    -> Kiểm tra đó là số chẵn hay số lẻ và là số âm hay dương
"""

while True:
    try:
        so_nguyen = int(input("Nhap so nguyen: "))
        print(f"So nguyen ban nhap: {so_nguyen}")
        break
    except ValueError:
        print("Chi duoc nhap so nguyen!")

if so_nguyen == 0:
    print(so_nguyen, "la so 0")

else:
    chan_le = "chan" if so_nguyen % 2 == 0 else "le"
    am_duong = "duong" if so_nguyen > 0 else "am"

    print(f"{so_nguyen} la so nguyen {am_duong} va la so {chan_le}")


# if so_nguyen == 0:
#     print(so_nguyen, "la so 0")
#
# elif so_nguyen % 2 == 0 and so_nguyen > 0:
#     print(so_nguyen, "la so nguyen duong va la so chan")
#
# elif so_nguyen % 2 == 0 and so_nguyen < 0:
#     print(so_nguyen, "la so nguyen am va la so chan")
#
# elif so_nguyen % 2 and so_nguyen > 0:
#     print(so_nguyen, "la so nguyen duong va la so le")
#
# elif so_nguyen % 2 and so_nguyen < 0:
#     print(so_nguyen, "la so nguyen am va la so le")