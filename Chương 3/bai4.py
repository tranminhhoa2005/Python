n = int(input("Nhập n (< 20): "))
if n >= 20:
    print("Nhập n nhỏ hơn 20")
else:
    for i in range(1, n):
        if i % 5 == 0 or i % 7 == 0:
            print(i)