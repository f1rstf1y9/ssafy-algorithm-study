T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, kind = input().split()
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1
    total = 1
    for kind in clothes.keys():
        total *= (clothes[kind]+1)
    print(total-1)