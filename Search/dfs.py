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