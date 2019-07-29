# https://www.acmicpc.net/problem/2667
# 주의해야할 점 : index 범위 / x, y좌표 순서

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def isInside(x, y):
    return (0 <= x < n and 0 <= y < n)

def bfs(size) :
    queue = []
    """
    전체적 흐름 : 
    n*n의 사이즈를 모두 확인한다.
    확인하다가 visited가 False라서 아직 방문하지 않았는데
    house값이 1이면 새로운 단지에 넣어줘야 하므로
    그 지점부터 시작해서 bfs를 수행하면서 
    상하 좌우를 확인하며 주변 집들을 다 묶는다.

    한 지점이 끝나면 다시 남은 n*n 집들을 찾아보는데
    거기서 visited가 True면 이미 방문했기 때문에 무시
    값이 0이면 집이 없기 때문에 무시
    그래서 아직 확인하지 않은 위치들만 
    새로 단지에 잘 넣을 수 있다.
    """


    for i in range (size): # 행 증가
        for j in range (size): # 열 증가
            """
            visited를 아직 방문하지 않아서 false인데
            그 위치의 값이 1이라는 의미는
            그 위치를 새로운 단지에 넣어야한다는 의미!

            그래서 그 지점부터 queue에 넣고 bfs를 돌기 시작한다.
            처음 시작한 주변(상하좌우)의 값이 1인 집들을 다 queue에 넣고,
            같은 단지에 묶일 수 있도록 한다.
            """
            if visited[i][j] is False and house[i][j] is 1:
                queue.append([i,j]) 
                # print("i,j =", i, j)
                # print("queue1 =", queue)
                """
                해당 위치를 queue에 넣으며 방문했기 때문에 
                visited를 True로 바꿔줘야하고, count도 올려줘야한다.
                count : 현재 단지의 집의 수
                """
                visited[i][j] = True 
                count = 1
                while queue:
                    y, x = queue.pop(0)
                    # print("queue2 =", queue)
                    # print("y,x =", y, x)
                    for q in range (4):
                        nx = x + dx[q]
                        ny = y + dy[q]
                        # print("ny, nx =", ny, nx)
                        # print("visited = ", visited)

                        if isInside(nx, ny) and visited[ny][nx] is False and house[ny][nx] is 1:
                            queue.append([ny,nx])
                            # print("queue3 =", queue)
                            visited[ny][nx] = True
                            # print("visited2 = ", visited)
                            count = count + 1
                            # print("count =", count)
                group.append(count)
                # group에 집의수를 추가하면 새로운 단지의 개수가 자동으로 늘어난다.


n = int(input())

# visited는 값을 수정하기 위해 False로 다 초기화
visited = [[False]*n for i in range (n)] 
house = []
group = []

for i in range(n):
    house.append(list(map(int, list(input()))))

bfs(n)
print(len(group))
group.sort() # 정렬하라는 문제 조건 따르기!
for i in range (len(group)):
    print(group[i])