"""
    Viết CT nhận input và xác đinh kiểu dữ liệu
    Thử convert thành int -> float -> boolean -> string

    -> In ra kiểu dữ liệu phù hợp nhất
"""

def xac_dinh_kieu_du_lieu(input_data):
    # Thu convert thanh int
    try:
        int_value = int(input_data)
        print(f"Co the convert thanh int: {int_value}")
        return "int"
    except ValueError:
        print("Khong the convert thanh int")

    # Thu convert thanh float
    try:
        float_value = float(input_data)
        print(f"Co the convert thanh float: {float_value}")
        return "float"
    except ValueError:
        print("Khong the convert thanh float")

    # Thu convert thanh boolean
    if input_data.lower() in ['true', 'false', '1', '0']:
        if input_data.lower() == 'true' or input_data == '1':
            bool_value = True
        else:
            bool_value = False
        print(f"Có thể convert thành boolean: {bool_value}")
        return "boolean"
    else:
        print("Không thể convert thành boolean")

    # Mac dinh la string
    print(f"Giu nguyen là string: {input_data}")
    return "str"

# Main
user_input = input("Nhap vao du lieu kiem tra: ")

print(f"Input ban dau la: '{user_input}' (kieu: {type(user_input).__name__})")
print("Thu convert:")

kieu_phu_hop = xac_dinh_kieu_du_lieu(user_input)

print(f"Kieu du lieu phu hop nhat: {kieu_phu_hop}")

# Test với nhiều trường hợp
# print("TEST VỚI CÁC TRƯỜNG HỢP KHÁC:")
#
# test_cases = ["123", "12.5", "true", "false", "hello", "0", "1", "-456"]
#
# for test in test_cases:
#     print(f"\n--- Test với '{test}' ---")
#     result = xac_dinh_kieu_du_lieu(test)
#     print(f"Kết quả: {result}")