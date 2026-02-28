import json
def f(s):
    i, n = 0, len(s)
    while i < n:
        if s[i] == '.':
            i += 1
            continue
        if s[i] == '[':
            i += 1
            j = i
            while j < n and s[j].isdigit():
                j += 1
            if j == i or j >= n or s[j] != ']':
                return None
            yield ("idx", int(s[i:j]))
            i = j + 1
        else:
            j = i
            while j < n and s[j] not in '.[':
                j += 1
            if j == i:
                return None
            yield ("key", s[i:j])
            i = j
def r(o, s):
    t = f(s)
    if t is None:
        return "NOT_FOUND"
    c = o
    for k, v in t:
        if k == "key":
            if not isinstance(c, dict) or v not in c:
                return "NOT_FOUND"
            c = c[v]
        else:
            if not isinstance(c, list) or not (0 <= v < len(c)):
                return "NOT_FOUND"
            c = c[v]
    return c
j = json.loads(input())
q = int(input())
for _ in range(q):
    p = input()
    otv = r(j, p)
    if otv == "NOT_FOUND":
        print("NOT_FOUND")
    else:
        print(json.dumps(otv, separators=(',', ':')))