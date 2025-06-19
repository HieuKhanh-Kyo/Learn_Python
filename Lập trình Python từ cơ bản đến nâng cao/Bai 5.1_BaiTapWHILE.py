# Viet CT nhap vao gio, phut, giay va 1 so giay là k nhap tu ban phim, sau do cong them k giay vao gio, phut, giay vua nhap roi in ra

# h = int(input("Enter hour = "))
# m = int(input("Enter minute = "))
# s = int(input("Enter second = "))
#
# k = int(input("Enter added second = "))

# C1: Khong dung vong lap

# total_S = (h * 3600 ) + (m * 60) + s  + k   # tong so giay
#
# h_New = total_S // 3600    # hoac dung:   int(total_S / 3600)
# m_New = (total_S - (h_New * 3600)) // 60
# s_New = (total_S - (h_New * 3600) - (m_New * 60))

# print(h_New, m_New, s_New)

# C2: Dung lenh lap while

# total_S = s + k
#
# while total_S >= 60:
#     m += total_S // 60
#     total_S -= (total_S // 60) * 60
#
# while m >= 60:
#     h += m // 60
#     m -= (m // 60) * 60
#
# print(h, m, total_S)


# Viet CT nhap vao mot so nguyen n tu ban phim, cho biet n co bao nhieu chu so va tinh tong cac chu so cua no

n = int(input("n = "))
so_chu_so = 0
s = 0

while n != 0:
    i = n % 10
    s += i
    n //= 10
    so_chu_so += 1

print("n co", so_chu_so, "chu so")
print("tong cac chu so:", s)

