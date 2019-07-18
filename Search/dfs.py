graph = {
'A': ['B'],
'B': ['A', 'C', 'D'],
'C': ['B', 'E'],
'D': ['B', 'F', 'G', 'H'],
'E': ['C'],
'F': ['D'],
'G': ['D'],
'H': ['D'],
}

#DFS
visited = []
stack = [] #FILO
stack.append('A')

while stack:
    check = stack.pop()

    if check not in visited:
        visited.append(check)
        stack.extend(graph[check])

print("DFS = ", visited)


#BFS
visited = []
queue = [] #FIFO
queue.append('A')

while queue:
    check = queue.pop(0)

    if check not in visited:
        visited.append(check)
        queue.extend(graph[check])

print("BFS = ", visited)