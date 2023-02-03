while 1:
    a,b,c = map(lambda x:x**2, map(int, input().split()))
    if a==0: break
    print("right" if 2*max(a,b,c)-(a+b+c)==0 else "wrong")