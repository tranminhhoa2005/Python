_list = ['hello', 'hi', 'python', 'is', 'great']
n = int(input("Nhập n: "))
_new = [ tu for tu in _list if len(tu) > n ]
print("Bài 11 - Từ có độ dài lớn hơn", n, ":", _new)