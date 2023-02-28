alpha = [0]*26
N = int(input())
for _ in range(N):
	n = input()
	for i in range(len(n)):
		alpha[ord(n[i])-65] += 10**(len(n)-i-1)
alpha.sort(reverse=True)
ans = 0
for i in range(10):
	ans += alpha[i]*(9-i)
print(ans)