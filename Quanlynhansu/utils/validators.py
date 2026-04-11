import re
from exceptions import InvalidAgeError, InvalidSalaryError

def validate_age(age):
    if not (18 <= age <= 65):
        raise InvalidAgeError("Tuổi phải nằm trong khoảng từ 18 đến 65.")
    return age

def validate_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError("Lương cơ bản phải lớn hơn 0.")
    return salary

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise ValueError("Email không đúng định dạng (ví dụ: ten@domain.com).")
    return email

def validate_performance_score(score):
    if not (0 <= score <= 10):
        raise ValueError("Điểm hiệu suất phải nằm trong khoảng từ 0 đến 10.")
    return score

def input_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val <= 0:
                print("Giá trị phải lớn hơn 0.")
                continue
            return val
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

def input_float_in_range(prompt, min_val, max_val):
    while True:
        try:
            val = float(input(prompt))
            if not (min_val <= val <= max_val):
                print(f"Giá trị phải từ {min_val} đến {max_val}.")
                continue
            return val
        except ValueError:
            print("Vui lòng nhập một số thực.")