from math import factorial as f
N, K = map(int, input().split())
print(f(N)//(f(N-K)*f(K)))