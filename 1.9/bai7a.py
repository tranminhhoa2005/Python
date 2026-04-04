_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
_new = [x for x in _list if _list.count(x) == 1]
print("Bài 7a:", _new)