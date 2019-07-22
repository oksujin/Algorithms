
def Search_Printer(result):
    print(" ".join(result))

#BFS
def bfs(graph, start):
    # for i in range(0, len(graph)):
    #    graph[i].sort()
    if graph[start] is []:
        print(start)
        return 

    visited = []
    queue = [start] #FIFO

    while queue:
        check = queue.pop(0)
        tmp = []
        if check not in visited:
            visited.append(check)
            tmp = list(set(graph[check])-set(visited))
            tmp.sort()
            queue.extend(tmp)
            # print("queue = ", queue)

    result = list(map(str,visited))
    Search_Printer(result)
    #print(visited)


#DFS
def dfs(graph, start):
    # for i in range(0, len(graph)):
    #     graph[i].sort(reverse=True)
    #     # graph[i].reverse는 순서만 거꾸로 바꿔준다!
    if graph[start] is []:
        print(start)
        return 
        
    visited = []
    stack = [start] #FILO
    # print("graph = ", graph)

    while stack:
        check = stack.pop()
        # print("check= ", check)
        tmp = []
        if check not in visited:
            visited.append(check)
            # print("visited =", visited)
            tmp = list(set(graph[check])-set(visited))
            tmp.sort(reverse=True)
            # print("tmp =", tmp)
            stack.extend(tmp)
            # print("stack =", stack)

    result = list(map(str,visited))
    Search_Printer(result)
    #print(visited)


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
