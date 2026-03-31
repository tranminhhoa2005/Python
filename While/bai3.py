n = int(input("Nhập n: "))
i = 2
la_ngt = True
while i * i <= n:
    if n % i == 0:
        la_ngt = False
        break
    i += 1

if n < 2:
    la_ngt = False

if la_ngt:
    print("Đây là số nguyên tố")
else:
    print("Không phải số nguyên tố")