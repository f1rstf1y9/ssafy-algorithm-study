N = int(input())
members = [(lambda l: (int(l[0]), l[1]))(input().split()) for _ in range(N)]


def quick_sort(tuples):
    if len(tuples) < 2:
        return tuples
    pivot = tuples[0]
    left = []
    right = []
    for tup in tuples[1:]:
        if tup[0] < pivot[0]:
            left.append(tup)
        else:
            right.append(tup)
    return quick_sort(left)+[pivot]+quick_sort(right)


for member in quick_sort(members):
    print(*member)
