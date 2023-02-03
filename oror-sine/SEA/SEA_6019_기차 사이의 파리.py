T = int(input())
for test in range(T):
    D, A, B, F = map(int, input().split())
    B *= -1
    pos_A, pos_B, pos_F = 0, D, 0
    is_forward = 1
    d = 0
    while abs(pos_A - pos_B) > 0.0000001:
        F_ = is_forward * F
        t = (pos_B - pos_F) / (F_ - B) if is_forward == 1 else (pos_F - pos_A) / (A - F_)
        pos_A += A * t
        pos_B += B * t
        pos_F += F_ * t
        d += F * t
        is_forward *= -1
    print(f"#{test+1}", d)
