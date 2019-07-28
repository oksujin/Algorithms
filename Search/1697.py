def isInside(x):
    return (0 <= x <= 100000)

def bfs(start, end):
    queue = [start]

    while queue:
        x = queue.pop(0)
        if x is end:
            return  

        for i in (x+1, x-1, x*2):
            if isInside(i) and visited[i] is -1:
                visited[i] = visited[x] + 1   
                queue.append(i)         
            
n, k = map(int, input().split())

visited = [-1]*100001
visited[n] = 0 # 시작하는 자리는 0으로 초기화

bfs(n, k)
print(visited[k])