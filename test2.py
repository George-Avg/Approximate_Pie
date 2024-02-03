# Approximate multiplier for starting position of x for pie approximation

from mpmath import mpf, mp

mp.dps = 10
pi = mpf('9.8696044010893586188344909998761511353136994072407906264133493762')


def f(n, x, num):
    return 10 ** (n / x) - num


def root(n, num):
    a = 1
    b = 3

    if f(n, a, num) < 0:
        min_val = a
        max_val = b

    else:
        min_val = b
        max_val = a

    while True:
        mid = (max_val + min_val) / 2
        dif = f(n, mid, num)
        if abs(dif) < 1e-100:
            return dif, mid
        elif dif > 0:
            max_val = mid
        else:
            min_val = mid


print(root(2, pi))
