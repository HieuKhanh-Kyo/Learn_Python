# Nhap vao 1 DS sinh vien gom: Ma, Ten sv, Lop. In ra DS sv ra man hinh, thong tin cua moi sv tren mot dong

DS_sv = {}
n = int(input("Nhap so luong sv = "))

for i in range(n):
    Ma = input("Ma: ")
    Ten = input("Ten: ")
    Lop = input("Lop: ")
    DS_sv[i] = f"Ma: {Ma},Ten: {Ten},Lop: {Lop}"

print("DS SV:")
for i in DS_sv:
    print(f"SV {i+1}. {DS_sv[i]}")             #print(DS_sv[i])

# DS_sv = []
# n = int(input("Nhap so luong sv = "))
#
# for i in range(n):
#     # tao bien sv kieu dict co key ma, ten, lop va rong
#     sv = {"Ma" : "", "Ten" : "", "Lop" : ""}
#
#     for j in sv:
#         print("Nhap ", j,":", end = "")
#         values = input()
#         sv[j] = values
#
#     DS_sv.append(sv)
#
# for i in range(n):
#     print("Thong tin sv", i+1, ":")
#     print("Ma:", DS_sv[i]["Ma"], "Ten:", DS_sv[i]["Ten"], "Lop:", DS_sv[i]["Lop"])