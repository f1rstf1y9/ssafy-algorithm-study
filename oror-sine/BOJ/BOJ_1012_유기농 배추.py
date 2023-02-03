T = int(input())
for _ in range(T):
    _, _, K = map(int, input().split())
    baechus = [tuple(map(int, input().split())) for _ in range(K)]
    
    cnt = 0  # 지렁이 수
    worm = {}  # 배추 : 입주 지렁이
    for baechu in baechus:  # 각각의 배추
        x, y = baechu
        neighbors = ((x-1, y),(x+1, y),(x, y-1),(x, y+1))  # 이웃 배추들
        neighbors_with_worm = []  # 분양된 이웃 배추 리스트
        neighbor_worms = []  # 이웃 지렁이_리스트
        goodbye_cnt = 0  # 빠이빠이할 지렁이 수
        for neighbor in neighbors:  # 각각의 이웃 배추에 대해서
            neighbor_worm = worm.get(neighbor)  # 이웃 배추에 입주한 지렁이
            if neighbor_worm and (neighbor_worm not in neighbor_worms):  # 이웃 지렁이가 있는데, 리스트에 없으면
                if len(neighbor_worms): goodbye_cnt +=1 # 다른 이웃 지렁이가 있으면 보낼 준비
                neighbor_worms.append(neighbor_worm)  # 이웃 지렁이 리스트에 추가하고
                neighbors_with_worm.append(neighbor)  # 분양된 배추 리스트에 추가
        else:
            if len(neighbor_worms):  # 이웃 지렁이가 있으면
                mini = min(neighbor_worms)  # 그 중에 가장 먼저 온 지렁이
                worm[baechu] = mini  # 가장 먼저 온 지렁이에게 배추 분양
                
                for neighbor in neighbors_with_worm:  # 각각의 분양된 이웃 배추
                    goodbye = worm[neighbor]  # 빠이빠이할 지렁이 
                    for home, host in worm.items():  
                        if host == goodbye:  # 빠이빠이할 지렁이가 살던 배추
                            worm[home] = mini  # 가장 먼저 온 지렁이한테 양도
                cnt -= goodbye_cnt  # 잘가 지렁이

            else:  # 이웃 지렁이 없으면 한 마리 새로 입주시킴
                cnt += 1
                worm[baechu] = cnt

    print(cnt)
