import json
def diff(a, b, path="", out=None):
    if out is None:
        out = []
    if isinstance(a, dict) and isinstance(b, dict):
        ks = set(a.keys()) | set(b.keys())
        for k in ks:
            p = f"{path}.{k}" if path else k
            if k not in a:
                out.append((p, "<missing>", json.dumps(b[k], separators=(',', ':'), sort_keys=True)))
            elif k not in b:
                out.append((p, json.dumps(a[k], separators=(',', ':'), sort_keys=True), "<missing>"))
            else:
                diff(a[k], b[k], p, out)
        return out
    if a != b:
        out.append((path, json.dumps(a, separators=(',', ':'), sort_keys=True), json.dumps(b, separators=(',', ':'), sort_keys=True)))
    return out
a = json.loads(input())
b = json.loads(input())
l = diff(a, b)
l.sort(key=lambda x: x[0])
if not l:
    print("No differences")
else:
    for p, ov, nv, in l:
        print(f"{p} : {ov} -> {nv}")