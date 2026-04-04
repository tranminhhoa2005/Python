_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
seen = []
_new = []
for x in _list:
    if x not in seen:
        _new.append(x)
        seen.append(x)
print("Bài 7b:", _new)