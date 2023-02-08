N = int(input())
A = list(map(int, input().split()))

cache = [1]*N
ans = 1

for i in range(1, N):
    temp = [cache[i]]
    for j in range(i):
        if A[j] < A[i]:
            temp.append(cache[j]+1)
    cache[i] = max(temp)
print(max(cache))