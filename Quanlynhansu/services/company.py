from exceptions import EmployeeNotFoundError, DuplicateEmployeeError

class Company:
    """Lớp quản lý danh sách nhân viên trong công ty"""
    def __init__(self):
        self.employees = {}   # key: emp_id, value: Employee object

    def add_employee(self, employee):
        """Thêm một nhân viên mới vào công ty"""
        if employee.emp_id in self.employees:
            raise DuplicateEmployeeError(f"ID {employee.emp_id} đã tồn tại trong hệ thống.")
        self.employees[employee.emp_id] = employee

    def remove_employee(self, emp_id):
        """Xóa nhân viên khỏi công ty (nghỉ việc)"""
        if emp_id not in self.employees:
            raise EmployeeNotFoundError(emp_id)
        del self.employees[emp_id]

    def get_employee(self, emp_id):
        """Lấy đối tượng nhân viên theo ID"""
        if emp_id not in self.employees:
            raise EmployeeNotFoundError(emp_id)
        return self.employees[emp_id]

    def get_all_employees(self):
        """Trả về danh sách tất cả nhân viên"""
        return list(self.employees.values())

    def get_employees_by_type(self, emp_type):
        """Trả về danh sách nhân viên theo loại (Manager/Developer/Intern)"""
        return [e for e in self.employees.values() if e.__class__.__name__ == emp_type]