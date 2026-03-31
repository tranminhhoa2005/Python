n = int(input("Nhập n: "))
gt = 1
i = 1
while i <= n:
    gt *= i
    i += 1
print(f"{n}! = {gt}")