T = int(input())
for t in range(T):
    N = int(input())

    closet = {}
    for _ in range(N):
        _, kind = input().split()
        if kind in closet.keys():
            closet[kind] += 1
        else:
            closet[kind] = 1

    tmp = 1
    for i in closet.values():
        tmp *= i+1

    print(tmp-1)
