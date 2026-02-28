r = float(input())
a, b = map(float, input().split())
c, d = map(float, input().split())
ABsq = (a - c) ** 2 + (b - d) ** 2
p = 2.0 * (a * (c - a) + b * (d - b))
delta = p * p - 4.0 * ABsq * (a * a + b * b - r * r)
eps = 1e-12
if delta < -eps:
    A_in = (a * a + b * b) <= r * r + eps
    B_in = (c * c + d * d) <= r * r + eps
    otvet = ABsq ** 0.5 if (A_in and B_in) else 0.0
else:
    delta = max(0.0, delta)
    sqrtd = delta ** 0.5
    t1 = (-p - sqrtd) / (2.0 * ABsq)
    t2 = (-p + sqrtd) / (2.0 * ABsq)
    if t1 > t2:
        t1, t2 = t2, t1
    left = max(0.0, t1)
    right = min(1.0, t2)
    otvet = max(0.0, right - left) * (ABsq ** 0.5)
print(f"{otvet:.10f}")