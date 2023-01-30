def solution(nums):
    poke = set(nums)
    N = len(nums)//2
    if len(poke) >= N:
        answer = N
    else:
        answer = len(poke)
    return answer