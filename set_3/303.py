s = input()
n0 = "ZER"
n1 = "ONE"
n2 = "TWO"
n3 = "THR"
n4 = "FOU"
n5 = "FIV"
n6 = "SIX"
n7 = "SEV"
n8 = "EIG"
n9 = "NIN"
p = 0
for i in range(len(s)):
    if s[i] == '+' or s[i] == '-' or s[i] == '*': p = i
c1 = 0
c2 = 0
for i in range(len(s) - 1, p, -3):
    sub = s[i - 2:i + 1]
    po = 10 ** ((len(s) - 1 - i) // 3)
    if sub == n1: c2 += po
    elif sub == n2: c2 += 2 * po
    elif sub == n3: c2 += 3 * po
    elif sub == n4: c2 += 4 * po
    elif sub == n5: c2 += 5 * po
    elif sub == n6: c2 += 6 * po
    elif sub == n7: c2 += 7 * po
    elif sub == n8: c2 += 8 * po
    elif sub == n9: c2 += 9 * po
for i in range(p - 1, -1, -3):
    sub = s[i - 2:i + 1]
    po = 10 ** ((p - 1 - i) // 3)
    if sub == n1: c1 += po
    elif sub == n2: c1 += 2 * po
    elif sub == n3: c1 += 3 * po
    elif sub == n4: c1 += 4 * po
    elif sub == n5: c1 += 5 * po
    elif sub == n6: c1 += 6 * po
    elif sub == n7: c1 += 7 * po
    elif sub == n8: c1 += 8 * po
    elif sub == n9: c1 += 9 * po
t = 0
if s[p] == '+': t = c1 + c2
elif s[p] == '-': t = c1 - c2
elif s[p] == '*': t = c1 * c2
ooo = ""
while t > 0:
    if t % 10 == 0: ooo = n0 + ooo
    elif t % 10 == 1: ooo = n1 + ooo
    elif t % 10 == 2: ooo = n2 + ooo
    elif t % 10 == 3: ooo = n3 + ooo
    elif t % 10 == 4: ooo = n4 + ooo
    elif t % 10 == 5: ooo = n5 + ooo
    elif t % 10 == 6: ooo = n6 + ooo
    elif t % 10 == 7: ooo = n7 + ooo
    elif t % 10 == 8: ooo = n8 + ooo
    elif t % 10 == 9: ooo = n9 + ooo
    t //= 10
print(ooo)