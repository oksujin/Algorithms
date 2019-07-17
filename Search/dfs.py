#DFS 수정
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
stack = [] #FILO
stack.append('A')

while stack:
    check = stack.pop()

    if check not in visited:
        visited.append(check)
        print("graph[check] =", graph[check])
        stack.extend(graph[check])
        print("stack =", stack)

print("visited= ", visited)