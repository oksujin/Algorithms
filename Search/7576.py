# https://www.acmicpc.net/problem/7576
# 토마토 문제
from collections import deque

# 상우하좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def isInside(x, y):
    return (0 <= x < m and 0 <= y < n)

# 토마토가 다 익었는지, 익는데 필요한 최대 날짜는 몇인지 확인
def checkMax():
    maxNum = 0
    #print(n, m)
    for i in range(n):
        for j in range (m):
            """
            만약 값이 초기화 값 그대로 0이라면
            주변에 -1로 막혀서 토마토가 익을 수 없는 것을 의미한다.
            그래서 -1을 반환
            """
            if check[i][j] is 0:
                return -1
            maxNum = max(maxNum, check[i][j])
    return maxNum-1
    """
    1이 들어가있는 자리의 1에 1을 더한 값으로 
    check[i][j]가 채워져있다. 하지만
    원래 1이 있는 자리가 채워지는데 필요한 횟수는 0이기 때문에
    결과에서 1을 빼주면 된다.
    """

def bfs():
    while queue:
        y, x = queue.popleft()
        for q in range (4):
            nx = x + dx[q]
            ny = y + dy[q]     

            if isInside(nx, ny) and box[ny][nx] is 0 and check[ny][nx] is 0:
                queue.append([ny,nx])
                check[ny][nx] = check[y][x] + 1
                # 1을 가진 자리의 수에서 하루 지났기 때문에 +1

m, n = map(int, input().split())
box = []
check = [[0]*m for i in range (n)]
queue = deque()

for i in range(n):
    tmp = list(map(int, input().split()))
    box.append(tmp)
    for j in range (len(tmp)):
        # box에 값을 넣으면서 만약 1이 있으면 queue에 넣어준다.
        if tmp[j] is 1:
            queue.append([i,j])
            check[i][j] = 1
        # box에 -1이 있으면 check에도 -1을 넣어준다.
        if tmp[j] is -1:
            check[i][j] = -1

bfs()
maxNum = checkMax()
print(maxNum)