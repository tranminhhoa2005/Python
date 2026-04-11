from abc import ABC, abstractmethod

class Employee(ABC):
    """Lớp trừu tượng đại diện cho nhân viên"""
    def __init__(self, emp_id, name, age, email, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.base_salary = base_salary
        self.performance_score = 5.0   # điểm hiệu suất mặc định
        self.projects = []              # danh sách tên dự án tham gia

    @abstractmethod
    def calculate_salary(self):
        """Phương thức trừu tượng tính lương – sẽ được các lớp con ghi đè"""
        pass

    def add_project(self, project_name):
        """Thêm một dự án vào danh sách dự án của nhân viên"""
        from exceptions import ProjectAllocationError
        if len(self.projects) >= 5:
            raise ProjectAllocationError(
                f"Nhân viên {self.emp_id} đã tham gia tối đa 5 dự án."
            )
        self.projects.append(project_name)

    def remove_project(self, project_name):
        """Xóa một dự án khỏi danh sách"""
        if project_name in self.projects:
            self.projects.remove(project_name)
        else:
            raise ValueError(
                f"Dự án '{project_name}' không có trong danh sách của nhân viên {self.emp_id}."
            )

    def __str__(self):
        return f"{self.emp_id} - {self.name} - {self.__class__.__name__}"