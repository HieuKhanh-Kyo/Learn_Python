# Xay dung ham:
# def <ten_ham>([<ds_tham_so>]):
#     <ds_cac_lenh>
#     return

# Xd ham tinh to hop chap k cua n: n! / (k!* (n - k)!)
def giai_thua(a):
    gt = 1
    for i in range(1, a+1):
        gt *= i
    return gt

kq = giai_thua(5) / (giai_thua(3) * giai_thua(5 - 3))
print(kq)

# Xd ham tinh UCLN cua 2 so
def UCLN(a, b):
    ucln = 1
    if a > b:
        a = b

    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            ucln = i
            break

    return ucln

# Xd ham tim gia tri lon nhat trong gia tri a,b
def max(a,b):
    if a > b:
        print("max =", a)
    else:
        print("max =", b)

max(10, 20)