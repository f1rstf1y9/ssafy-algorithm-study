def move_robot():
    new_robot = []
    new_pos = [0]*(2*N)
    for i in range(len(robot)):
        p = (robot[i]+1)%(2*N)
        if not robot_pos[p] and A[p]:
            A[p] -= 1
            robot_pos[robot[i]] = 0
            if p != down:
                new_robot.append(p)
                new_pos[p] = 1
            else:
                continue
        else:
            new_robot.append(robot[i])
            new_pos[robot[i]] = 1
    return new_robot, new_pos

N, K = map(int, input().split())
A = list(map(int, input().split()))
up, down = 0, N-1
robot = []
robot_pos = [0]*(2*N)
ans = 0
while A.count(0) < K:
    # 벨트 회전
    up = (up-1)%(2*N)
    down = (down-1)%(2*N)

    # 내리는 위치에 있는 로봇 즉시 내리기
    if robot_pos[down]:
        robot_pos[down] = 0
        robot.remove(down)

    # 로봇 이동방향으로 이동 - 이동하려는 칸에 로봇x, 내구도 1이상
    robot, robot_pos = move_robot()

    # 올리는 위치에 로봇 올리기
    if A[up]:
        robot.append(up)
        robot_pos[up] = 1
        A[up] -= 1
    ans += 1
print(ans)
