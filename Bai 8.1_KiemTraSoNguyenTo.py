# Xay dung ham tim so nguyen to va in ra tat ca so nguyen to tu 2 den 100
import math

# def tim_so_nguyen_to(*args):
#     snt = []
#     for i in args:
#         if i <= 2:
#             snt.append(i)
#         for j in range(2, int(math.sqrt(i)) + 1):                   #range(2, i)
#             if i % j == 0:
#                 break
#         else:
#             snt.append(i)
#     return snt
#
# def main():
#     print("Cac so nguyen to la", tim_so_nguyen_to(*range(2,101)))
#
# main()


def kiem_tra_snt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    for i in range(2,101):
        if kiem_tra_snt(i) == True:
            print(i, " ", end = "")               # in tren 1 dong

main()
