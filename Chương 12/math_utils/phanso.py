def cong(a, b, c, d):
    tu = a * d + b * c
    mau = b * d
    return tu, mau

def tru(a, b, c, d):
    tu = a * d - b * c
    mau = b * d
    return tu, mau

def nhan(a, b, c, d):
    tu = a * c
    mau = b * d
    return tu, mau

def chia(a, b, c, d):
    tu = a * d
    mau = b * c
    return tu, mau