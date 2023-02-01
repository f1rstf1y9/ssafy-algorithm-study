for t in range(10):
    N = int(input())
    heights = list(map(int, input().split()))
    
    maxi = 0
    maxi_idx = 0
    mini = 0
    mini_idx = 0
    for _ in range(N):
        maxi = heights[99]
        maxi_idx = 99
        mini = heights[99]
        mini_idx = 99
        for i in range(99):
            height = heights[i]
            if mini > heights[i]:
                mini, mini_idx = height, i 
            if maxi < heights[i]:
                maxi, maxi_idx = height, i 
        heights[mini_idx] += 1 
        heights[maxi_idx] -= 1
    else:
        maxi = heights[99]
        mini = heights[99]
        for i in range(99):
            height = heights[i]
            if mini > heights[i]:
                mini=height
            if maxi < heights[i]:
                maxi=height
        print(f"#{t+1}", maxi-mini) 
