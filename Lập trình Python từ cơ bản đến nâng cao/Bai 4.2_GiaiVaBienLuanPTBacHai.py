# ax^2 + bx + c = 0

# delta = b^2 - 4ac

# Neu a != 0
# Neu delta >0, pt co 2 nghiem phan biet
#   x1 = (-b + sqrt(delta)) / 2a)
#   x2 = (-b - sqrt(delta)) / 2a)
# Neu delta == 0, pt co nghiem kep
#   x1 = x2 = -b / 2a
# Neu delta <0, pt vo nghiem

# Neu a == 0
# Neu b != 0 -> x = -b/a
# Neu b == 0
#   neu c == 0 -> vo so nghiem
#   neu c != 0 -> vo nghiem

import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = b*b - 4*a*c

if a != 0:
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print ("x1 = ", x1, "\nx2 = ", x2)

    elif delta == 0:
        x1 = x2 = - b/ 2*a
        print("x1 = x2 = ", x1)

    else:
        print("PT vo nghiem")

else:
    if b != 0:
        x = -b/a
        print("x = ", x)

    else:
        if c == 0:
            print("PT vo so nghiem")
        else:
            print("PT vo nghiem")