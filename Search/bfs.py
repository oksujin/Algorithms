#DFS
graph = {
'A': ['B'],
'B': ['A', 'C', 'H'],
'C': ['B', 'D'],
'D': ['C', 'E', 'G'],
'E': ['D', 'F'],
'F': ['E'],
'G': ['C'],
'H': ['B', 'I', 'J', 'M'],
'I': ['H'],
'J': ['H', 'K'],
'K': ['J', 'L'],
'L': ['K'],
'M': ['H']
}
visited = []
queue = [] #FIFO
queue.append('A')

while queue:
    check = queue.pop(0)

    if check not in visited:
        visited.append(check)
        print("graph[check] =", graph[check])
        queue.extend(graph[check])
        print("queue =", queue)

print("visited= ", visited)