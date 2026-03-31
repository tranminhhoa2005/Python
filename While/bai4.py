n = int(input("Nhập n: "))
tong = 0
i = 1
while i < n:
    if i % 2 == 0:
        tong += i
    i += 1
print(f"Tổng = {tong}")