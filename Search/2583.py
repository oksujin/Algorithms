# https://www.acmicpc.net/problem/2583
# 영역구하기

from collections import deque

def isInside(x, y):
    return (0 <= x < m and 0 <= y < n)

def bfs():
    queue = deque()
    
    for i in range (m):
        count = 0
        for j in range (n):
            if isInside(i,j) and maps[i][j] is 0:
                queue.append([i,j])
                maps[i][j] = 1
                while queue:         
                    y, x = queue.popleft()           
                    count = count + 1
                    
                    



# 5, 7, 3
m, n, k = map(int, input().split())
maps = [[0]*n for i in range (m)]
num = []

for i in range (k):
    a, b, c, d = list(map(int, input().split()))
    for q in range (b, d):
        for p in range (a, c):
            maps[q][p] = 1

for i in range(m):
    print(maps[i])        

bfs()
print(len(bfs))
print(bfs)