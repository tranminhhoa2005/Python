from .employee import Employee

class Intern(Employee):
    """Lớp Intern kế thừa từ Employee"""
    def __init__(self, emp_id, name, age, email, base_salary, university, semester):
        super().__init__(emp_id, name, age, email, base_salary)
        self.university = university
        self.semester = semester

    def calculate_salary(self):
        """Lương Intern = 80% lương cơ bản"""
        return self.base_salary * 0.8