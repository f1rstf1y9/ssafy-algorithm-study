import sys
def decomposition_sum(N):
    return int(N)+sum(list(map(int, str(N))))

def min_generator(N):
    for i in range(N):
        if decomposition_sum(i)==N:
            return i
    return 0

N = int(sys.stdin.readline())
print(min_generator(N))