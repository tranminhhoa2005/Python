import time

x = time.localtime()
year = x[0]

_nam_sinh = int(input("Nhập năm sinh: "))
_tuoi = year - _nam_sinh
print(f"Năm sinh {_nam_sinh}, vậy bạn {_tuoi} tuổi.")