def format_currency(amount):
    """Định dạng số tiền thành chuỗi có dấu phân cách hàng nghìn và VND"""
    return f"{amount:,.0f} VND"

def display_employee_list(employees):
    """Hiển thị danh sách nhân viên dưới dạng bảng đơn giản"""
    if not employees:
        print("Danh sách trống.")
        return

    print(f"{'ID':<10} | {'Họ tên':<20} | {'Loại':<12} | {'Lương':>15}")
    print("-" * 65)
    for emp in employees:
        salary = emp.calculate_salary()
        print(f"{emp.emp_id:<10} | {emp.name:<20} | {emp.__class__.__name__:<12} | {format_currency(salary):>15}")