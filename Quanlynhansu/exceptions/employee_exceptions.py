class EmployeeException(Exception):
    """Lớp ngoại lệ cơ sở cho toàn bộ hệ thống nhân viên"""
    pass

class EmployeeNotFoundError(EmployeeException):
    """Ngoại lệ khi không tìm thấy nhân viên theo ID"""
    def __init__(self, employee_id):
        self.employee_id = employee_id
        super().__init__(f"Không tìm thấy nhân viên có ID: {employee_id}")

class InvalidSalaryError(EmployeeException):
    """Ngoại lệ khi lương không hợp lệ (<= 0)"""
    pass

class InvalidAgeError(EmployeeException):
    """Ngoại lệ khi tuổi nằm ngoài khoảng 18-65"""
    pass

class ProjectAllocationError(EmployeeException):
    """Ngoại lệ khi phân công dự án vượt quá giới hạn (tối đa 5 dự án)"""
    pass

class DuplicateEmployeeError(EmployeeException):
    """Ngoại lệ khi thêm nhân viên có ID đã tồn tại"""
    pass