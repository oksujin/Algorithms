# https://www.acmicpc.net/problem/2583
# 영역구하기
from collections import deque

# 상우하좌 : list기준(수학적 좌표기준x)
"""
list[x][y]에서 
위로 가려면 앞에 들어가는 x축이 -1
아래로 가려면 앞에 들어가는 x축이 +1
오른쪽으로 가려면 뒤에 들어가는 y축이 +1
왼쪽으로 가려면 뒤에 들어가는 y축이 -1
"""
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def isInside(x, y):
    return (0<= x < m and 0 <= y < n)

def bfs():
    count = 1
    while queue:
        x, y = queue.popleft()
        # 상우하좌 네 방향 모두 확인 
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isInside(nx, ny) and maps[nx][ny] is 0:
                count = count + 1 # 개수를 올려주고
                maps[nx][ny] = 1 # 넘어갔을 때 다시 확인하지 않기 위해 1로 바꾼다.
                queue.append([nx, ny])
    num.append(count) # 다 계산한 후, 개수를 num에 넣어준다.

m, n, k = map(int, input().split())
maps = [[0]*n for i in range (m)]

"""
0 2 4 4
를 입력받게 되는데,
이 좌표를 (2,0) (4, 4)로 뒤집어서 생각하면
2-4까지 0-4까지의 범위로 잡아서
x, y의 증가를 쉽게 표현할 수 있다.

즉, 왼쪽 아래와 오른쪽 위의 점을 찍던 것을
왼쪽 위와 오른쪽 아래로 찍는다고 보면 된다.
"""
for i in range (k):
    a,b,c,d = map(int, input().split())
    for q in range (b, d):
        for p in range (a, c):
            maps[q][p] = 1

# 출력확인용
# print(m,n,k)
# for i in range (m):
#     print(maps[i])

queue = deque()
num = []

"""
모든 위치를 다 확인하면서 0이 있는 포인트에서 bfs
queue에 들어가는 순간 0을 1로 바꾸기 때문에
한번 queue에 들어가면 다시 확인하지 않는다.
"""
for i in range(m):
    for j in range (n):
        if isInside(i,j) and maps[i][j] is 0:
            queue.append([i,j])
            maps[i][j] = 1
            bfs()

print(len(num))
# int형이라 map으로 str로 바꿔줘야한다.
print(" ".join(map(str, sorted(num))))

