import datetime
def f(s):
    dp, tp = s.strip().split()
    y, m, d = map(int, dp.split("-"))
    sign = 1 if tp[3] == "+" else -1
    h, mi = map(int, tp[4:].split(":"))
    offset = sign * (h * 3600 + mi * 60)
    l = datetime.datetime(y, m, d, 0, 0, 0)
    return int(l.timestamp()) - offset
a = f(input())
b = f(input())
days = abs(a - b) // 86400
print(days)