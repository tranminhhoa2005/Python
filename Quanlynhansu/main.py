import sys
from models import Manager, Developer, Intern
from services import Company, total_company_salary, top_n_highest_salary
from utils import (
    validate_age,
    validate_salary,
    validate_email,
    validate_performance_score,
    input_positive_int,
    input_float_in_range,
    display_employee_list
)
from exceptions import EmployeeNotFoundError, ProjectAllocationError, DuplicateEmployeeError

# ---------- Các hàm hỗ trợ nhập liệu ----------
def add_employee_flow(company, emp_type):
    """Quy trình thêm một nhân viên mới (Manager/Developer/Intern)"""
    try:
        emp_id = input("Nhập mã nhân viên: ").strip()
        name = input("Nhập họ tên: ").strip()
        age = validate_age(int(input("Nhập tuổi: ")))
        email = validate_email(input("Nhập email: ").strip())
        base_salary = validate_salary(float(input("Nhập lương cơ bản: ")))

        if emp_type == "Manager":
            bonus_rate_input = input("Nhập tỷ lệ thưởng (mặc định 0.25): ").strip()
            bonus_rate = float(bonus_rate_input) if bonus_rate_input else 0.25
            emp = Manager(emp_id, name, age, email, base_salary, bonus_rate)

        elif emp_type == "Developer":
            lang = input("Nhập ngôn ngữ lập trình: ").strip()
            overtime = input_positive_int("Nhập số giờ làm thêm (mặc định 0): ")
            emp = Developer(emp_id, name, age, email, base_salary, lang, overtime)

        elif emp_type == "Intern":
            uni = input("Nhập trường đại học: ").strip()
            semester = input("Nhập học kỳ: ").strip()
            emp = Intern(emp_id, name, age, email, base_salary, uni, semester)

        else:
            print("Loại nhân viên không hợp lệ.")
            return

        company.add_employee(emp)
        print(f"✅ Đã thêm {emp_type} {emp_id} thành công.")

    except DuplicateEmployeeError as e:
        print(f"❌ {e}")
        new_id = emp_id + "_new"
        print(f"Gợi ý ID mới: {new_id}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

# ---------- Các menu con ----------
def payroll_menu(company):
    """Menu quản lý lương"""
    while True:
        print("\n--- QUẢN LÝ LƯƠNG ---")
        print("1. Tính lương từng nhân viên")
        print("2. Tổng lương công ty")
        print("3. Top 3 lương cao nhất")
        print("4. Quay lại")
        choice = input("Chọn: ").strip()

        if choice == '1':
            for emp in company.get_all_employees():
                salary = emp.calculate_salary()
                print(f"{emp.emp_id} - {emp.name}: {salary:,.0f} VND")
        elif choice == '2':
            total = total_company_salary(company)
            print(f"Tổng lương toàn công ty: {total:,.0f} VND")
        elif choice == '3':
            top3 = top_n_highest_salary(company, 3)
            display_employee_list(top3)
        elif choice == '4':
            break
        else:
            print("Lựa chọn không hợp lệ.")

def project_management_menu(company):
    """Menu quản lý dự án"""
    while True:
        print("\n--- QUẢN LÝ DỰ ÁN ---")
        print("1. Phân công nhân viên vào dự án")
        print("2. Xóa nhân viên khỏi dự án")
        print("3. Hiển thị dự án của 1 nhân viên")
        print("4. Quay lại")
        choice = input("Chọn: ").strip()

        if choice == '1':
            emp_id = input("Nhập ID nhân viên: ").strip()
            proj = input("Tên dự án: ").strip()
            try:
                emp = company.get_employee(emp_id)
                emp.add_project(proj)
                print(f"✅ Đã thêm dự án '{proj}' cho nhân viên {emp_id}")
            except (EmployeeNotFoundError, ProjectAllocationError) as e:
                print(f"❌ {e}")

        elif choice == '2':
            emp_id = input("Nhập ID nhân viên: ").strip()
            proj = input("Tên dự án cần xóa: ").strip()
            try:
                emp = company.get_employee(emp_id)
                emp.remove_project(proj)
                print(f"✅ Đã xóa dự án '{proj}' khỏi nhân viên {emp_id}")
            except (EmployeeNotFoundError, ValueError) as e:
                print(f"❌ {e}")

        elif choice == '3':
            emp_id = input("Nhập ID nhân viên: ").strip()
            try:
                emp = company.get_employee(emp_id)
                if emp.projects:
                    print(f"Dự án của {emp_id}: {', '.join(emp.projects)}")
                else:
                    print("Nhân viên chưa tham gia dự án nào.")
            except EmployeeNotFoundError as e:
                print(f"❌ {e}")

        elif choice == '4':
            break
        else:
            print("Lựa chọn không hợp lệ.")

def performance_menu(company):
    """Menu đánh giá hiệu suất"""
    while True:
        print("\n--- ĐÁNH GIÁ HIỆU SUẤT ---")
        print("1. Cập nhật điểm hiệu suất")
        print("2. Nhân viên xuất sắc (>8)")
        print("3. Nhân viên cần cải thiện (<5)")
        print("4. Quay lại")
        choice = input("Chọn: ").strip()

        if choice == '1':
            emp_id = input("Nhập ID nhân viên: ").strip()
            try:
                emp = company.get_employee(emp_id)
                new_score = input_float_in_range("Nhập điểm hiệu suất (0-10): ", 0, 10)
                emp.performance_score = new_score
                print(f"✅ Đã cập nhật điểm cho nhân viên {emp_id}")
            except EmployeeNotFoundError as e:
                print(f"❌ {e}")

        elif choice == '2':
            excellent = [e for e in company.get_all_employees() if e.performance_score > 8]
            display_employee_list(excellent)

        elif choice == '3':
            weak = [e for e in company.get_all_employees() if e.performance_score < 5]
            display_employee_list(weak)

        elif choice == '4':
            break
        else:
            print("Lựa chọn không hợp lệ.")

def hr_management_menu(company):
    """Menu QUẢN LÝ NHÂN SỰ (chức năng 7)"""
    while True:
        print("\n--- QUẢN LÝ NHÂN SỰ ---")
        print("1. Xóa nhân viên (nghỉ việc)")
        print("2. Tăng lương cơ bản cho nhân viên")
        print("3. Thăng chức (Intern -> Developer, Developer -> Manager)")
        print("4. Quay lại")
        choice = input("Chọn: ").strip()

        if choice == '1':
            emp_id = input("Nhập ID nhân viên cần xóa: ").strip()
            try:
                company.remove_employee(emp_id)
                print(f"✅ Đã xóa nhân viên {emp_id} khỏi hệ thống.")
            except EmployeeNotFoundError as e:
                print(f"❌ {e}")

        elif choice == '2':
            emp_id = input("Nhập ID nhân viên cần tăng lương: ").strip()
            try:
                emp = company.get_employee(emp_id)
                increase = float(input("Nhập số tiền tăng thêm: "))
                if increase <= 0:
                    print("Số tiền tăng phải lớn hơn 0.")
                    continue
                emp.base_salary += increase
                print(f"✅ Lương cơ bản mới của {emp_id} là {emp.base_salary:,.0f} VND")
            except (EmployeeNotFoundError, ValueError) as e:
                print(f"❌ {e}")

        elif choice == '3':
            emp_id = input("Nhập ID nhân viên cần thăng chức: ").strip()
            try:
                old_emp = company.get_employee(emp_id)

                if isinstance(old_emp, Intern):
                    # Intern -> Developer
                    new_dev = Developer(
                        old_emp.emp_id,
                        old_emp.name,
                        old_emp.age,
                        old_emp.email,
                        old_emp.base_salary * 1.2,   # tăng 20%
                        input("Nhập ngôn ngữ lập trình chính: ").strip(),
                        0
                    )
                    new_dev.performance_score = old_emp.performance_score
                    new_dev.projects = old_emp.projects.copy()
                    company.remove_employee(emp_id)
                    company.add_employee(new_dev)
                    print(f"✅ Intern {emp_id} đã được thăng chức lên Developer.")

                elif isinstance(old_emp, Developer):
                    # Developer -> Manager
                    new_mgr = Manager(
                        old_emp.emp_id,
                        old_emp.name,
                        old_emp.age,
                        old_emp.email,
                        old_emp.base_salary * 1.3,   # tăng 30%
                        0.25
                    )
                    new_mgr.performance_score = old_emp.performance_score
                    new_mgr.projects = old_emp.projects.copy()
                    company.remove_employee(emp_id)
                    company.add_employee(new_mgr)
                    print(f"✅ Developer {emp_id} đã được thăng chức lên Manager.")

                else:
                    print("❌ Chỉ có thể thăng chức Intern -> Developer hoặc Developer -> Manager.")

            except EmployeeNotFoundError as e:
                print(f"❌ {e}")
            except Exception as e:
                print(f"❌ Lỗi: {e}")

        elif choice == '4':
            break
        else:
            print("Lựa chọn không hợp lệ.")

def statistics_menu(company):
    """Menu thống kê báo cáo"""
    while True:
        print("\n--- THỐNG KÊ BÁO CÁO ---")
        print("1. Số lượng nhân viên theo loại")
        print("2. Tổng lương theo phòng ban (chưa triển khai phòng ban)")
        print("3. Số dự án trung bình trên mỗi nhân viên")
        print("4. Quay lại")
        choice = input("Chọn: ").strip()

        if choice == '1':
            type_counts = {}
            for emp in company.get_all_employees():
                t = emp.__class__.__name__
                type_counts[t] = type_counts.get(t, 0) + 1
            for t, count in type_counts.items():
                print(f"{t}: {count} nhân viên")

        elif choice == '2':
            print("⚠️ Chức năng đang được phát triển (chưa có dữ liệu phòng ban).")

        elif choice == '3':
            emps = company.get_all_employees()
            if not emps:
                print("Chưa có nhân viên nào.")
                continue
            avg = sum(len(e.projects) for e in emps) / len(emps)
            print(f"Trung bình mỗi nhân viên tham gia {avg:.2f} dự án.")

        elif choice == '4':
            break
        else:
            print("Lựa chọn không hợp lệ.")

# ---------- Hàm main ----------
def main():
    company = Company()

    while True:
        print("\n" + "=" * 50)
        print("HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC")
        print("=" * 50)
        print("1. Thêm nhân viên mới")
        print("2. Hiển thị danh sách nhân viên")
        print("3. Tìm kiếm nhân viên")
        print("4. Quản lý lương")
        print("5. Quản lý dự án")
        print("6. Đánh giá hiệu suất")
        print("7. Quản lý nhân sự")
        print("8. Thống kê báo cáo")
        print("9. Thoát")
        choice = input("Chọn chức năng (1-9): ").strip()

        if choice == '1':
            print("\n  a. Thêm Manager")
            print("  b. Thêm Developer")
            print("  c. Thêm Intern")
            sub = input("Chọn (a/b/c): ").strip().lower()
            if sub == 'a':
                add_employee_flow(company, "Manager")
            elif sub == 'b':
                add_employee_flow(company, "Developer")
            elif sub == 'c':
                add_employee_flow(company, "Intern")
            else:
                print("Lựa chọn không hợp lệ.")

        elif choice == '2':
            print("\n  a. Tất cả nhân viên")
            print("  b. Theo loại (Manager/Developer/Intern)")
            print("  c. Theo hiệu suất (từ cao đến thấp)")
            sub = input("Chọn: ").strip().lower()
            if sub == 'a':
                display_employee_list(company.get_all_employees())
            elif sub == 'b':
                t = input("Nhập loại nhân viên (Manager/Developer/Intern): ").strip()
                emps = company.get_employees_by_type(t)
                display_employee_list(emps)
            elif sub == 'c':
                sorted_emps = sorted(
                    company.get_all_employees(),
                    key=lambda e: e.performance_score,
                    reverse=True
                )
                display_employee_list(sorted_emps)
            else:
                print("Lựa chọn không hợp lệ.")

        elif choice == '3':
            print("\n  a. Theo ID")
            print("  b. Theo tên")
            print("  c. Theo ngôn ngữ lập trình (Developer)")
            sub = input("Chọn: ").strip().lower()
            if sub == 'a':
                emp_id = input("Nhập ID cần tìm: ").strip()
                try:
                    emp = company.get_employee(emp_id)
                    print(f"Tìm thấy: {emp}")
                    print(f"  Lương: {emp.calculate_salary():,.0f} VND")
                    print(f"  Điểm hiệu suất: {emp.performance_score}")
                    print(f"  Dự án: {', '.join(emp.projects) if emp.projects else 'Không có'}")
                except EmployeeNotFoundError as e:
                    print(f"❌ {e}")
            elif sub == 'b':
                keyword = input("Nhập tên cần tìm: ").strip().lower()
                results = [e for e in company.get_all_employees() if keyword in e.name.lower()]
                display_employee_list(results)
            elif sub == 'c':
                lang = input("Nhập ngôn ngữ lập trình: ").strip().lower()
                devs = company.get_employees_by_type("Developer")
                results = [d for d in devs if lang in d.programming_language.lower()]
                display_employee_list(results)
            else:
                print("Lựa chọn không hợp lệ.")

        elif choice == '4':
            payroll_menu(company)

        elif choice == '5':
            project_management_menu(company)

        elif choice == '6':
            performance_menu(company)

        elif choice == '7':
            hr_management_menu(company)

        elif choice == '8':
            statistics_menu(company)

        elif choice == '9':
            print("👋 Thoát chương trình. Tạm biệt!")
            sys.exit(0)

        else:
            print("Vui lòng chọn số từ 1 đến 9.")

if __name__ == "__main__":
    main()