n = int(input("Nhập n: "))

if n > 10:
    print(f"{n} lớn hơn 10")
else:
    for i in range(0, n + 1):
        if i % 2 == 0:
            print(i)
end = input("Nhấn Enter để kết thúc chương trình...")            