# 상하좌우의 x,y좌표 이동 위치를 나타내는 list들
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start, end):
    least[0][0] = 1
    visited[0][0] = False
    queue = [start]

    while queue:
        x, y = queue.pop(0) # 확인할 위치의 좌표를 받아온다
        for i in range (0, 4): # 확인할 위치에서의 상하좌우 확인하기 위한 for문
            # nx, ny는 현재 좌표에서 상하좌우로 한칸 이동한 좌표를 의미한다.
            nx = x + dx[i] 
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m: # 해당 위치가 n*m 안에 있을 때만 작동
                # 아직 방문하지 않았고, maps에서 1의 값이 들어있을 때만 작동
                if visited[nx][ny] == False and maps[nx][ny] == 1: 
                    queue.append([nx,ny]) # 이동한 위치도 확인해주기 위해 queue에 추가
                    visited[nx][ny] = True # 방문했다는 표시로 변경
                    least[nx][ny] = least[x][y] + 1 # 현재 위치에서의 최소 방문회수 넣어준다
    print(least[end[0]][end[1]])

n, m = map(int, input().split()) # n=4, m=6

# list라서 배열을 넣어줘야 해당자리 값 변경 가능. 아니면 append로 넣어줘야함
maps = [[0]*m for i in range (n)]
visited = [[False]*m for i in range (n)]
least = [[0]*m for i in range (n)]

# string, int형 잘 지정해줘야한다.
for i in range (0, n):
    tmp = str(input())
    for j in range (0, m):
        maps[i][j] = int(tmp[j])

# 0,0 부터 3,5까지 확인한다
bfs([0,0], [n-1, m-1])
