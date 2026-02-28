import json
def app(s, p):
    if isinstance(s, dict) and isinstance(p, dict):
        r = dict(s)
        for k, v in p.items():
            if v is None:
                r.pop(k, None)
            elif k in r and isinstance(r[k], dict) and isinstance(v, dict):
                r[k] = app(r[k], v)
            else:
                r[k] = v
        return r
    return p
s = json.loads(input())
p = json.loads(input())
r = app(s, p)
print(json.dumps(r, separators=(',', ':'), sort_keys=True))