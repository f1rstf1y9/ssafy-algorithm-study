for t in range(10):
    N = int(input())
    heights = tuple(map(int, input().split()))
    total = 0
    for i in range(2, N-1):
        houses = heights[i]
        left = heights[i-2:i]
        right = heights[i+1:i+3]

        maxi = 0
        for height in left+right:
            if maxi < height:
                maxi = height
                
        total += houses-maxi if houses > maxi else 0

    print(f"#{t+1}", total)