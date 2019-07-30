# https://www.acmicpc.net/problem/2178
# 상하좌우의 x,y좌표 이동 위치를 나타내는 list들
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start, end):
    least[0][0] = 1
    visited[0][0] = False
    queue = [start]

    while queue:
        y, x = queue.pop(0) # 확인할 위치의 좌표를 받아온다
        for i in range (0, 4): # 확인할 위치에서의 상하좌우 확인하기 위한 for문
            # nx, ny는 현재 좌표에서 상하좌우로 한칸 이동한 좌표를 의미한다.
            nx = x + dx[i] 
            ny = y + dy[i]
            """
            처음에 x, y에 (0,0)을 받아온 후 x와 dy를 더해주면
            nx = 0, ny = -1이 나온다.

            상을 표시하기 위해 더해줬는데 만약
            [nx][ny] 순서로 넣게되면 (0,-1)이 되므로 좌를 나타낸다.
            따라서 우리가 의도한대로 나타내기 위해서는
            [ny][nx] 순서로 넣어줘야한다. 

            이것이 배열이 반대라고 말하는 이유이다.
            """
            
         if 0 <= nx < m and 0 <= ny < n: # 해당 위치가 n*m 안에 있을 때만 작동
                # 아직 방문하지 않았고, maps에서 1의 값이 들어있을 때만 작동
                if visited[ny][nx] == False and maps[ny][nx] == 1: 
                    queue.append([ny,nx]) # 이동한 위치도 확인해주기 위해 queue에 추가
                    visited[ny][nx] = True # 방문했다는 표시로 변경
                    least[ny][nx] = least[y][x] + 1 # 현재 위치에서의 최소 방문회수 넣어준다
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
