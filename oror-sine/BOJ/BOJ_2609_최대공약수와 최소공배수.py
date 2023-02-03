def euclidean_algorithm(a,b):
    g,l = (a,b) if a>b else (b,a)
    r = g%l
    return euclidean_algorithm(l,r) if r else l
GCD = euclidean_algorithm

def LCM(a,b):
    return a*b//GCD(a,b)

a,b = map(int, input().split())
print(GCD(a,b))
print(LCM(a,b))