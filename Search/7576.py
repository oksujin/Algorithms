

m, n = map(int, input().split())

box = []
for i in range(n):
    tmp = list(map(int, input().split()))
    box.append(tmp)
print(box)


visited = [[False]*m for i in range (n)]

for i in range(n): # 0-4
    for j in range(m): # 0-6
        if(box[i][j] is -1):
            visited[i][j] = -1

print(visited)