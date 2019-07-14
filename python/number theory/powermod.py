# なんか違うっぽいですねー
def modpower(a, n, mod):
    res = 1
    y = a
    while n > 0:
        if n % 2 == 1:
            res = res * y % mod
        y = (y ** 2) % mod
        n /= 2
    return res
