import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    fs = tuple(input().strip())
    _ = int(input())
    arr = input()
    arr_list = []
    tmp = ""
    R = idx = 0
    for c in range(len(arr)):
        if arr[c].isdigit():
            tmp += arr[c]
        elif tmp:
            arr_list.append(tmp)
            tmp = ""
    else:
        if tmp:
            arr_list.append(tmp)
    try:
        for f in fs:
            if f == "R":
                R += 1
                idx = -1 if idx == 0 else 0
            elif f == "D":
                arr_list.pop(idx)
        else:
            if R % 2:
                arr_list = arr_list[::-1]
            print("["+",".join(arr_list)+"]")
    except:
        print("error")
