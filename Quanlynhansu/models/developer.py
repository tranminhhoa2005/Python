from .employee import Employee

class Developer(Employee):
    """Lớp Developer kế thừa từ Employee"""
    def __init__(self, emp_id, name, age, email, base_salary, programming_language, overtime_hours=0):
        super().__init__(emp_id, name, age, email, base_salary)
        self.programming_language = programming_language
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        """Lương Developer = lương cơ bản + tiền làm thêm giờ (50.000 VND/giờ)"""
        return self.base_salary + self.overtime_hours * 50_000