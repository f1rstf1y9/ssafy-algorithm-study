from collections import Counter

def solution(participant, completion):
    answer = ''
    part = Counter(participant)
    comp = Counter(completion)
    for p in part:
        if p not in comp:
            answer = p
            break
        elif part[p] != comp[p]:
            answer = p
            break
    return answer