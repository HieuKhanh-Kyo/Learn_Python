# ax + b = 0
# a != 0  -> x = -b / a
# a = 0
#   b = 0 -> x = vo so nghiem
#   b != 0 -> x = vo nghiem

a = float(input("a = "))
b = float(input("b = "))

# x = 0
#
# if a != 0:
#     x = -b/a
# else:
#     if b == 0:
#         x = "vo so nghiem"
#     else:
#         x = "vo nghiem"
#
# print("Nghiem cua pt la ", x)

if a != 0:
    x = -b/a
    print("x = ", -b/a)
else:
    if b == 0:
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
