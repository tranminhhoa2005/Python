# ============ B1 ============
# Đọc n dòng đầu tiên của file cho trước

def b1():
    ten_file = input("Nhập tên file: ")
    n = int(input("Nhập số dòng muốn đọc: "))
    with open(ten_file, "r", encoding="utf-8") as f:
        for i, dong in enumerate(f):
            if i >= n:
                break
            print(dong, end="")


# ============ B2 ============
# Ghi đoạn văn bản vào file rồi hiển thị lại

def b2():
    ten_file = input("Nhập tên file để ghi: ")
    print("Nhập văn bản (gõ 'END' ở dòng mới để kết thúc):")
    dong_van_ban = []
    while True:
        dong = input()
        if dong == "END":
            break
        dong_van_ban.append(dong)

    with open(ten_file, "w", encoding="utf-8") as f:
        f.write("\n".join(dong_van_ban))

    print("\n--- Nội dung file ---")
    with open(ten_file, "r", encoding="utf-8") as f:
        print(f.read())


# ============ B3 ============
# Tạo demo_file1.txt rồi in theo 2 cách

def b3():
    with open("demo_file1.txt", "w", encoding="utf-8") as f:
        f.write("Thuc \n hanh \n voi \n file\n IO\n")

    # a) In trên một dòng
    with open("demo_file1.txt", "r", encoding="utf-8") as f:
        noi_dung = f.read()
    print("a) Một dòng:", noi_dung.replace("\n", " "))

    # b) In từng dòng
    print("b) Từng dòng:")
    with open("demo_file1.txt", "r", encoding="utf-8") as f:
        for dong in f:
            print(dong, end="")


# ============ B4 ============
# Nhập thông tin cá nhân, lưu vào setInfo.txt, đọc lại hiển thị

def b4():
    ten = input("Tên: ")
    tuoi = input("Tuổi: ")
    email = input("Email: ")
    skype = input("Skype: ")
    dia_chi = input("Địa chỉ: ")
    noi_lam_viec = input("Nơi làm việc: ")

    with open("setInfo.txt", "w", encoding="utf-8") as f:
        f.write(f"Tên: {ten}\n")
        f.write(f"Tuổi: {tuoi}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Skype: {skype}\n")
        f.write(f"Địa chỉ: {dia_chi}\n")
        f.write(f"Nơi làm việc: {noi_lam_viec}\n")

    print("\n--- Thông tin đã lưu ---")
    with open("setInfo.txt", "r", encoding="utf-8") as f:
        print(f.read())


# ============ B5 ============
# Đếm số lần xuất hiện của từng từ trong file

def b5():
    # Tạo file demo_file2.txt
    with open("demo_file2.txt", "w", encoding="utf-8") as f:
        f.write("Dem so luong tu xuat hien abc abc abc 12 12 it it eaut")

    with open("demo_file2.txt", "r", encoding="utf-8") as f:
        noi_dung = f.read()

    dem = {}
    for tu in noi_dung.split():
        dem[tu] = dem.get(tu, 0) + 1

    print("Kết quả:", dem)


# ============ MENU ============
def menu():
    while True:
        print("\n===== BÀI TẬP FILE I/O =====")
        print("1. B1 - Đọc n dòng đầu file")
        print("2. B2 - Ghi văn bản vào file")
        print("3. B3 - Tạo demo_file1.txt và in nội dung")
        print("4. B4 - Nhập thông tin cá nhân")
        print("5. B5 - Đếm từ trong file")
        print("0. Thoát")
        chon = input("Chọn: ")

        if chon == "1": b1()
        elif chon == "2": b2()
        elif chon == "3": b3()
        elif chon == "4": b4()
        elif chon == "5": b5()
        elif chon == "0": break
        else: print("Không hợp lệ!")

if __name__ == "__main__":
    menu()