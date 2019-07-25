def isInside(x, y):
    return (0<= x < w and 0 <= y < h)


def BFS(start, end):
    dist[0][0] = 1
    visit[0][0] = False
    queue = [start]
    
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            # 해당 방향의 좌표가 존재하고, 갈 수 있는 길이며, 방문하지 않은 경우
            if isInside(nx, ny) and maze[ny][nx] == 1 and visit[ny][nx] == False:
                # 해당 좌표 큐에 추가
                queue.append([ny, nx])
                visit[ny][nx] = True            # 해당 좌표 방문으로 설정
                dist[ny][nx] = dist[y][x] + 1   # 해당 좌표까지의 거리 현재 이동한 거리 + 1 로 초기화
    print(dist[end[0]][end[1]]) 


h, w = map(int, input().split())

maze = [[0]*w for i in range(h)]
visit = [[False]*w for i in range(h)]
dist = [[0]*w for i in range(h)]

for i in range(h):
    tmp = str(input())
    for j in range(len(tmp)):
        maze[i][j] = int(tmp[j])

# 상하좌우
dx = [0,0,1,-1]
dy = [-1,1,0,0]

BFS([0,0],[h-1,w-1])