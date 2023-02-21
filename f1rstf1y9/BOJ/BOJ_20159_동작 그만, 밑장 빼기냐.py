N = int(input())
cards = list(map(int, input().split()))
o_sum = [0]
e_sum = [0]
for i in range(0,N,2):
    o_sum.append(o_sum[-1] + cards[i])
    e_sum.append(e_sum[-1] + cards[i+1])
res = [o_sum[-1]]
for i in range(N//2):
    res.append(o_sum[i]+e_sum[-1]-e_sum[i])
    res.append(o_sum[i+1]+e_sum[-2]-e_sum[i])
print(max(res))