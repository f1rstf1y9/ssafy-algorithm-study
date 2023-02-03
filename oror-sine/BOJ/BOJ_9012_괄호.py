T = int(input())
for t in range(T):
    s = input()
    while "()" in s:
        s = s.replace("()","")
    print("NO" if s else "YES")
