s = "ca hanh an cu hanh"

print(s.capitalize())
# .capitalize()  Viết hoa chữ cái đầu tiên trong chuỗi

print(s.upper())
# .upper() viết hoa toàn bộ chuỗi

print(s.lower())
# .lower() chuyen toan bo chuoi tu chu hoa sang chu thuong

print(s.title())
# .title()  chuyen ky tu dau moi tu sang in hoa

s1= "***ca hanh co nhieu tien****"

print(s1.strip("*"))
# .strip() xoa ky tu duoc chi dinh o dau va cuoi chuoi

print(s1.lstrip("*"))
# .lstrip() xoa ky tu duoc chi dinh o ben trai chuoi

s2= "Ca Hanh mua Cu Hanh"

print(s2.split(" ",3))
# .split() tach cac ky tu trong chuoi thanh cac phan tu

print(s2.count("C", 5, 18))
# .count()  dem so lan xuat hien chuoi con trong chuoi me

print (s2.find("Cu"))
# .find()  tim chuoi con trong chuoi goc, tra ve vi tri chu dau tien tim dc, neu k tim thay thi tra ve -1

x = ["Luong", "Hieu", "Khanh"]
y = " ".join(x)

print(y)
# .join()  noi chuoi,  <ky tu noi>.join(tham so)

a = "hanh di mua hanh, nhung cho het hanh roi"

print (a.replace("hanh","toi",2))
# .replace()  Thay the chuoi con trong chuoi goc
