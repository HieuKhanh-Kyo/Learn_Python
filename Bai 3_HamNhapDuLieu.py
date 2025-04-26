# a = int(input())

# Goi thu vien:  import <ten thu vien> as <bi danh>
import math as m
import numpy as np  #lap trinh AI

b = m.sqrt(16)
c= np.array([1, 2, 3, 4, 5])

# print(b)
# Goi ham:  <ten_thu_vien> . <ten ham> (danh sach doi so cua ham)


# Viet CT tinh the tich hinh cau

import math

r = float(input("Enter radius = "))
V = round(4/3 * math.pi * r**3, 2)

print("The tich hinh cau la ", V)

# Viet CT tinh the tich hinh lap phuong

# l = float(input("Enter length = "))
# w = float(input("Enter withth = "))
# h = float(input("Enter height = "))
#
# v = l*w*h
#
# print(round(v,2))

import math

c = float(input("Enter edge of cube = "))
v = math.pow(c, 3)

print("Volume of cube = ", round(v, 3))