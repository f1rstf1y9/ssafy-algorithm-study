N, M = map(int, input().split())
cards = list(map(int, input().split()))
combination = 0
for i in range(N):
    if combination == M:break
    for j in range(N):
        if combination == M:break
        for k in range(N):
            if i!=j and j!=k and k!= i:
                _sum = cards[i]+cards[j]+cards[k]
                if _sum<=M and M-_sum<M-combination:
                    combination = _sum
                    if combination == M:break
print(combination)