import sys
_ = sys.stdin.readline()
owns = tuple(sys.stdin.readline().split())
_ = sys.stdin.readline()
keys = tuple(sys.stdin.readline().split())

cnt = {card: 0 for card in keys}
for own in owns:
    if own in cnt.keys():
        cnt[own] += 1

print(*(cnt[key] for key in keys))
