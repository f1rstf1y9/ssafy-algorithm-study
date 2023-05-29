import math
min_v, max_v = map(int, input().split())
max_double = int(math.sqrt(max_v))
checked = set()
for i in range(2,max_double+1):
    j = min_v // (i**2)
    while (i**2)*j <= max_v:
        if min_v <= (i**2)*j:
            checked.add((i**2)*j)
        j += 1
print(max_v-min_v+1-len(checked))
