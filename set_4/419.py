import math
r = float(input())
ax, ay = map(float, input().split())
bx, by = map(float, input().split())
def dist(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)
def ins(x, lo, hi):
    return max(lo, min(hi, x))
dx = bx - ax
dy = by - ay
seg2 = dx * dx + dy * dy
if seg2 == 0:
    print(0.0)
else:
    t = -(ax * dx + ay * dy) / seg2
    t = ins(t, 0.0, 1.0)
    px = ax + t * dx
    py = ay + t * dy
    m = math.hypot(px, py)
    if m >= r:
        print(f"{dist(ax, ay, bx, by):.10f}")
    else:
        da = math.hypot(ax, ay)
        db = math.hypot(bx, by)
        cos_theta = ins((ax * bx + ay * by) / (da * db), -1.0, 1.0)
        theta = math.acos(cos_theta)
        alpha = math.acos(ins(r / da, -1.0, 1.0))
        beta = math.acos(ins(r / db, -1.0, 1.0))
        tan_a = math.sqrt(max(0.0, da * da - r * r))
        tan_b = math.sqrt(max(0.0, db * db - r * r))
        arc_angle = theta - alpha - beta
        if arc_angle < 0:
            arc_angle = 0.0
        ans = tan_a + tan_b + r * arc_angle
        print(f"{ans:.10f}")