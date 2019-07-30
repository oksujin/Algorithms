# https://www.acmicpc.net/problem/7576
# 토마토 문제
from collections import deque

# 상우하좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

"""
visited 안에 False가 하나라도 있으면 False 출력
-1과 True로만 채워져있다면 True 출력

비워진 자리(-1)가 있더라도 나머지 0들이
다 채워지면 다 -1과 True가 되므로 True 출력
"""
def checkAll():
    for i in range (n):
        for j in range (m):
            if visited[i][j] is False:
                return False
    return True

def isInside(x, y):
    return (0 <= x < m and 0 <= y < n)

def bfs():
    queue = deque()
    count = 0

    while(True):
        tag = 0
        # 전체를 확인하면서 1이면서 아직 방문하지 않은 토마토들의 위치를 queue에 넣는다.
        for i in range (n):
            for j in range (m):
                if box[i][j] is 1 and visited[i][j] is False:
                    queue.append([i,j])
                    visited[i][j] = True
                    tag = 1 # visited에 변화가 있으면 tag 1로 변경

        # visited를 True로 바꿔준 후, 결과를 확인해서 다 True면 종료
        if tag is 1 and checkAll() : 
            return count
        # visited에 더 이상 변화가 없는데 False가 있다면 -1 return
        elif tag is 0:
            return -1
        else :
            count = count + 1
            while queue:
                y, x = queue.popleft()
                for q in range (4):
                    nx = x + dx[q]
                    ny = y + dy[q]

                    """
                    queue에 들어있는 1의 값을 가진 토마토들의 상하좌우를 확인하며
                    그 자리의 값을 1로 변경해준다.
                    """
                    if isInside(nx, ny) and box[ny][nx] is 0 and visited[ny][nx] is False:
                        box[ny][nx] = 1            

m, n = map(int, input().split())

box = []
for i in range(n):
    tmp = list(map(int, input().split()))
    box.append(tmp)

"""
visited에 
box가 0이면 False, box가 1이면 True
box가 -1이면 -1을 넣어서 초기화한다.
"""
visited = [[False]*m for i in range (n)]
for i in range(n): # 0-4
    for j in range(m): # 0-6
        if(box[i][j] is -1):
            visited[i][j] = -1

count = bfs()
print(count)