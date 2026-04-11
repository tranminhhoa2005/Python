def calculate_salary_for_employee(employee):
    """Tính lương cho một nhân viên"""
    return employee.calculate_salary()

def total_company_salary(company):
    """Tính tổng lương toàn công ty"""
    return sum(emp.calculate_salary() for emp in company.get_all_employees())

def top_n_highest_salary(company, n=3):
    """Trả về danh sách n nhân viên có lương cao nhất"""
    sorted_emps = sorted(
        company.get_all_employees(),
        key=lambda e: e.calculate_salary(),
        reverse=True
    )
    return sorted_emps[:n]