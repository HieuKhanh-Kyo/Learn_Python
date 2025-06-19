'''
Viết chương trình C để tính cước điện thoại bàn cho một hộ gia đình với các thông số như sau:

            Phí thuê bao bắt buộc là 25 nghìn.

            600 đồng cho mỗi phút gọi của 50 phút đầu tiên.

            400 đồng cho mỗi phút gọi của 150 phút tiếp theo.

            200 đồng cho bất kỳ phút gọi nào sau 200 phút đầu tiên.
'''

# input = int(input("Nhap so phut"))
# print(type(input))
#
# output = 25
#
# if input <= 50:
#     output = output + 600*input
# elif input <= 200:
#     output = output + 600*50 + 400*(input-50)
# else:
#     output = output + 600*50 + 400*150 + 200*(input-200)
#
# print("Cuoc dien thoai la:", output)

'''
Viết chương trình tính tiền điện gồm các khoảng sau:

            – Tiền thuê bao điện kế: 1000đ/tháng

            – Định mức sử dụng điện cho mỗi hộ là: 50 KW với giá 230đ/KW

            – Nếu phần vượt định mức <= 50KW thì tính giá 480đ/KW

            – Nếu 50KW < phần vượt định mức < 100KW thì tính giá 700đ/KW

            – Nếu phần vượt định mức >= 100KW thì tính giá 900đ/KW

            Chỉ số mới và cũ được nhập vào từ bàn phím

            – In ra màn hình chỉ số cũ, chỉ số mới, tiền trả định mức, tiền trả vượt định mức, tổng tiền phải trả.
'''

cu = int(input("Nhap chi so cu"))
moi = int(input("Nhap chi so moi"))

so_dien = moi - cu

tong_tien = 1000

if so_dien < 50:
    tong_tien = tong_tien + so_dien*230

elif so_dien <= 100:
    tong_tien = tong_tien + 50*230 + (so_dien - 50)*480

elif so_dien <150:
    tong_tien = tong_tien + 50*230 + (so_dien - 50)*700

else:
    tong_tien = tong_tien + 50*230 + (so_dien - 50)*900

print("tien tra dinh muc la")
print("tien tra vuot dinh muc la")
print("tong tien la", tong_tien)

