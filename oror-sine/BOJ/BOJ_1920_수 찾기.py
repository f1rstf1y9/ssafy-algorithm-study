import sys
input = sys.stdin.readline
input()
_set = set(map(int, input().split()))
input()
for i in list(map(int, input().split())):
    print(1 if i in _set else 0)