def bfs(start, end):
    dist[0][0] = 1
    visit[0][0] = False
    queue=[start]

    while queue :
        y, x = queue.pop(0)
        # 상하좌우 모두 확인
        for i in range (0, 4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 최소경로는 무조건 bfs / 경로의 수는 dfs
            # if 0 <= nx < m and 0 <= ny < n: # 범위 안인지 확인
            if 0 <= nx < m and 0 <= ny < n and visit[ny][nx] == False and map[ny][nx] == 1:
                queue.append([ny,nx])
                visit[ny][nx] = True
                dist[ny][nx] = dist[y][x] + 1
    print(dist[end[1]][end[0]])


n, m = map(int, input().split())

map = [[0]*m for i in range(n)] # list라 먼저 초기화
dist = [[0]*m for i in range(n)]
visit = [[False]*m for i in range(n)]

for i in range (0, n):
    tmp = str(input())
    for j in range (0, m):
        map[i][j] = int(tmp[j])

# 상하좌우 / dx, dy의 index 같이 이동함
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

bfs([0,0], [m-1,n-1])

