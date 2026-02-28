from datetime import date
EPOCH_ORD = date(1970, 1, 1).toordinal()
def is_leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
def parse_line(line):
    dpart, tz = line.strip().split()
    y, m, d = map(int, dpart.split("-"))
    sign = 1 if tz[3] == '+' else -1
    hh, mm = map(int, tz[4:].split(":"))
    offset_sec = sign * (hh * 3600 + mm * 60)
    return y, m, d, offset_sec
def utc_seconds_at_local_midnight(y, m, d, offset_sec):
    base = (date(y, m, d).toordinal() - EPOCH_ORD) * 86400
    return base - offset_sec
by, bm, bd, birth_off = parse_line(input())
cy, cm, cd, curr_off  = parse_line(input())
current_utc = utc_seconds_at_local_midnight(cy, cm, cd, curr_off)
def birthday_utc_for_year(Y):
    day = bd
    if bm == 2 and bd == 29 and not is_leap(Y):
        day = 28
    return utc_seconds_at_local_midnight(Y, bm, day, birth_off)
cand = birthday_utc_for_year(cy)
if cand < current_utc:
    cand = birthday_utc_for_year(cy + 1)
delta = cand - current_utc
days_left = (delta + 85399) // 86400
if days_left < 0:
    days_left = 0
print(days_left)