from .employee import Employee

class Manager(Employee):
    """Lớp Manager kế thừa từ Employee"""
    def __init__(self, emp_id, name, age, email, base_salary, bonus_rate=0.25):
        super().__init__(emp_id, name, age, email, base_salary)
        self.bonus_rate = bonus_rate

    def calculate_salary(self):
        """Lương Manager = lương cơ bản + thưởng theo tỉ lệ"""
        return self.base_salary * (1 + self.bonus_rate)