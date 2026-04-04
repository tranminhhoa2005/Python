_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
do_dai = int(input("Nhập độ dài: "))
dem = 0
for x in _list:
    if len(x) > do_dai and x[0] == x[-1]: 
        dem += 1
print("Bài 12 - Số chuỗi thỏa mãn điều kiện:", dem)