# Nam nhuan co thang 2 co 29 ngay:
# là nam chia het cho 4 nhung khong chia het cho 100 hoac chia het cho 400

month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month in {1, 3, 5, 7, 8, 10, 12}:
    print("Thang", month, "co 31 ngay")
elif month in {4, 6, 9, 11}:
    print("Thang", month, "co 30 ngay")
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Thang", month, "co 29 ngay")
    else:
        print("Thang", month, "co 28 ngay")