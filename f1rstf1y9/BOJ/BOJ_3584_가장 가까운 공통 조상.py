T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0] * (N+1)
    for _ in range(N-1):
        A, B = map(int, input().split())
        parent[B] = A
    nA, nB = map(int, input().split())
    pA, pB = [nA], [nB]
    while parent[nA]:
        pA.append(parent[nA])
        nA = parent[nA]
    while parent[nB]:
        pB.append(parent[nB])
        nB = parent[nB]

    while pA and pB and pA[-1] == pB[-1]:
        ans = pA.pop()
        pB.pop()
    print(ans)