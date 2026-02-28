import datetime
def f(s):
    dp, tp, tz = s.strip().split()
    y, m, d = map(int, dp.split("-"))
    H, M, S = map(int, tp.split(":"))
    sign = 1 if tz[3] == "+" else -1
    h, mi = map(int, tz[4:].split(":"))
    offset = sign * (h * 3600 + mi * 60)
    l = datetime.datetime(y, m, d, H, M, S)
    return int(l.timestamp()) - offset
a = f(input())
b = f(input())
print(b - a)