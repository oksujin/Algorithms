
#BFS
def bfs(graph, start):
    for i in range(0, len(graph)):
       graph[i].sort()

 
    visited = []
    queue = [] #FIFO
    queue.append(start)

    while queue:
        check = queue.pop(0)
        if check not in visited:
            visited.append(check)
            queue.extend(graph[check])

    print(visited)


#DFS
def dfs(graph, start):
    for i in range(0, len(graph)):
        graph[i].sort(reverse=True)
        # graph[i].reverse는 순서만 거꾸로 바꿔준다!

    visited = []
    stack = [] #FILO
    stack.append(start)

    while stack:
        check = stack.pop()

        if check not in visited:
            visited.append(check)
            stack.extend(graph[check])

    print(visited)


vertex, edge, start = list(map(int, input().split()))

graph = []
graph.append([])
for i in range(1, vertex+1):
    graph.append([])

for i in range(1, edge+1):
    v1, v2 = list(map(int, input().split()))

    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(graph, start)
bfs(graph, start)
