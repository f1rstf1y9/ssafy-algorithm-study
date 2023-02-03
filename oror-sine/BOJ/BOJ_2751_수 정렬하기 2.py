import sys
input=sys.stdin.readline
N = int(input())
for i in sorted([int(input()) for _ in range(N)]):
    print(i)