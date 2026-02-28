import importlib
q = int(input())
for _ in range(q):
    m, a = input().split()
    try:
        mod = importlib.import_module(m)
    except Exception:
        print("MODULE_NOT_FOUND")
        continue
    if not hasattr(mod, a):
        print("ATTRIBUTE_NOT_FOUND")
        continue
    o = getattr(mod, a)
    print("CALLABLE" if callable(o) else "VALUE")