def tinh_tong_2_so(a, b):
    return a + b


def tinh_tong_nhieu_so(*args):
    return sum(args)


def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def tim_nguyen_to_trong_khoang(a, b):
    return [n for n in range(a, b + 1) if kiem_tra_nguyen_to(n)]


def kiem_tra_so_hoan_hao(n):
    if n < 2:
        return False
    tong = sum(i for i in range(1, n) if n % i == 0)
    return tong == n


def tim_hoan_hao_trong_khoang(a, b):
    return [n for n in range(a, b + 1) if kiem_tra_so_hoan_hao(n)]


def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Tính tổng 2 số")
        print("2. Tính tổng nhiều số")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm số nguyên tố trong khoảng [a, b]")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm số hoàn hảo trong khoảng [a, b]")
        print("0. Thoát")
        print("================")

        chon = input("Chọn chức năng: ")

        if chon == "1":
            a = float(input("Nhập số a: "))
            b = float(input("Nhập số b: "))
            print(f"Tổng: {tinh_tong_2_so(a, b)}")

        elif chon == "2":
            nhap = input("Nhập các số cách nhau bằng dấu cách: ")
            so_list = list(map(float, nhap.split()))
            print(f"Tổng: {tinh_tong_nhieu_so(*so_list)}")

        elif chon == "3":
            n = int(input("Nhập số n: "))
            if kiem_tra_nguyen_to(n):
                print(f"{n} là số nguyên tố.")
            else:
                print(f"{n} không phải số nguyên tố.")

        elif chon == "4":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            ket_qua = tim_nguyen_to_trong_khoang(a, b)
            print(f"Số nguyên tố trong [{a}, {b}]: {ket_qua}")

        elif chon == "5":
            n = int(input("Nhập số n: "))
            if kiem_tra_so_hoan_hao(n):
                print(f"{n} là số hoàn hảo.")
            else:
                print(f"{n} không phải số hoàn hảo.")

        elif chon == "6":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            ket_qua = tim_hoan_hao_trong_khoang(a, b)
            print(f"Số hoàn hảo trong [{a}, {b}]: {ket_qua}")

        elif chon == "0":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ, thử lại!")


if __name__ == "__main__":
    menu()