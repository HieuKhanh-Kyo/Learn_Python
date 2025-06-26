"""
    Nhập vào số tiền VND, tỷ giá USD 1 USD = 24000 VND
    -> Chuyển đổi và hiển thị số tiền USD (làm tròn 2 chữ số thập phân)
"""

while True:
    TienVND = float(input("Nhap vao so tien VND = "))
    if TienVND > 0:
        break

TienUSD = round(TienVND / 24000, 2)

print(f"Chuyen tu {TienVND} VND thanh {TienUSD} USD")