def isInside(x, y):
    return (0 <= x <= n and 0 <= y <= n)

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(size) :
    queue = []
    group = []

    for i in range (size):
        for j in range (size):
            if visited[j][i] is False and house[j][i] is 1:
                queue.append([j,i])
                count = 1
                while queue:
                    y, x = queue.pop(0)
                    for q in range (4):
                        nx = x + dx[q]
                        ny = y + dy[q]
                    
                        if isInside(nx, ny) and visited[ny][nx] is False and house[ny][nx] is 1:
                            queue.append([ny,nx])
                            visited[ny][nx] = True
                            count = count + 1
                group.append(count)




n = int(input())

visited = [[False]*n] *n
house = []
group = [3, 5, 7]

for i in range(n):
    house.append(list(map(int, list(input()))))

bfs(n)
print(len(group))
for i in range (len(group)):
    print(group[i])
