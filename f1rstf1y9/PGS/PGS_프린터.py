def solution(priorities, location):
    docs = [[i, priorities[i]] for i in range(len(priorities))]
    cnt = 0
    while docs:
        p = priorities.pop(0)
        d = docs.pop(0)
        if not priorities:
            return cnt + 1
        if d[1] < max(priorities):
            docs.append(d)
            priorities.append(p)
        else:
            cnt += 1
            if d[0] == location:
                return cnt
    return cnt