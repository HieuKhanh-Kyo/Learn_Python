# Kieu tu dien dict:  <key> : <value>

# Khai bao bien kieu tu dien
thong_tin_sv = {"Ma SV" : 2021606652,
                "Ho va Ten" : "Luong Hieu Khanh",
                "Que quan" : "Bac Giang",
                "Chuyen nganh" : "QTKD"}
# print(type(thong_tin_sv))

# <ten_dict>[<key>]         Truy cap vao gia tri cua 1 key trong dict
# <ten_dict>.get(<key>)
# print(thong_tin_sv["Ho va Ten"])
# print(thong_tin_sv.get("Chuyen nganh"))

# <ten_dict>.values()       In ra tat ca value trong bien kieu tu dien
# print(thong_tin_sv.values())

# <ten_dict>.keys()         In ra tat ca cac key trong bien kieu tu dien
# print(thong_tin_sv.keys())

# Duyet qua tat ca cac phan tu trong kieu tu dien:

# for i in thong_tin_sv:
#     print(i, ":", thong_tin_sv[i])

# Nhap gia tri cho kieu tu  dien

# thong_tin_sv_1 = {}
# n = int(input("Nhap n ="))
#
# for i in range(n):
#     keys = input()
#     values = input()
#     thong_tin_sv_1[keys] = values
#
# print(thong_tin_sv_1)

# <ten_dict>.__delitem__(<key>)     xoa cap key : value tuong ung trong dict
# thong_tin_sv.__delitem__("Que quan")
# for i in thong_tin_sv:
#     print(i, ":", thong_tin_sv[i])

# <ten_dict>.clear()                xoa toan bo key, value trong dict, tro ve rong
thong_tin_sv.clear()
print(thong_tin_sv)
