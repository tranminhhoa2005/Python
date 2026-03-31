n = int(input("Nhập số nguyên dương: "))

chia2 = n % 2 == 0
chia3 = n % 3 == 0

if chia2 and chia3:
    print(f"{n} chia hết cho cả 2 và 3")
elif chia2:
    print(f"{n} chia hết cho 2 nhưng không chia hết cho 3")
elif chia3:
    print(f"{n} chia hết cho 3 nhưng không chia hết cho 2")
else:
    print(f"{n} không chia hết cho 2 cũng không chia hết cho 3")