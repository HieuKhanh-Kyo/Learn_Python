# Truyen tham so voi cac gia tri bat buoc
# def hoan_vi(a, b):
#     a, b = b, a
#     print(a, b)
#
# def main():
#     print(hoan_vi(1, 2))
#
# main()

# Truyen tham so voi gia tri mac dinh
# import math
#
# def dien_tich_hinh_tron(r = 0):
#     s = math.pi * r * r
#     return s
#
# def main():
#     print("Dien tich hinh tron la:", dien_tich_hinh_tron(2))
#
# main()

#Truyen tham so la tu khoa
# def dien_tich_hcn(a, b):
#     s = a * b
#     return s
#
# def main():
#     print("Dien tich hcn la:", dien_tich_hcn(a = 4, b = 6))

# Truyen tham so tuy y

#tim gia tri lon nhat trong cac gia tri nhap vao tu ban phim
def gt_max(*args):
    n = len(args)
    if n == 0:
        return
    else:
        max = args[0]
        for i in range(1, n):
            if max < args[i]:
                max = args[i]
    return max

def main():
    print("Gia tri lon nhat la:", gt_max(5,5,8,2,8,4,12,10))

main()