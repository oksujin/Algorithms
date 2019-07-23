# 백준 1260 DFS와 BFS


def Search_Printer(result):
    print(" ".join(result))
    """
    join은 앞의 " "를 기준으로 
    입력받은 list(result)를 문자열(string)으로
    변환해주는 함수다.
    """

#BFS
def bfs(graph, start):    
    """
    처음에 들어온 노드가 연결되지 않은 경우 
    시작 노드만 출력하고 종료하는 코드

    하지만 나는 list라서 각 그래프 자리에 []가 있으므로
    굳이 이 부분을 실행하지 않아도 while문에서
    if문에 들어가지 않아서(check가 추가되지 않기 때문에)
    start 노트만 visited에 들어가고 출력되고 끝나기 때문에
    이 코드 실행하지 않아도 된다.

    # if graph[start] is []:
    #     print(start)
    #     return 
    """
    visited = []
    queue = [start] #FIFO

    while queue:
        check = queue.pop(0)
        tmp = [] # 새로 입력 받아올 그래프의 노드들을 받아오는 list(인접행렬)
        if check not in visited:
            visited.append(check)
            """
            set : 집합 자료형을 만든다
            중복을 허용하지 않고, 순서가 없다
            (교집합 : & / 합집합 : | / 차집합 : -)

            차집합을 만들어서 새로 들어가는 노드에서
            방문한 노드를 빼기 위해서 사용한다.
            (방문한 노드는 다시 방문하지 않기 위해 사용)

            그 후, 정렬을 위해 다시 list로 만든다.
            """
            tmp = list(set(graph[check])-set(visited)) 
            tmp.sort()
            queue.extend(tmp)

    """
    visited는 현재 list이기 때문에,
    list에 들어있는 원소들을 string으로 바꾼 후,
    list로 만들어서 result에 넣고 출력한다.
    """
    result = list(map(str,visited))
    Search_Printer(result)

#DFS
def dfs(graph, start):
    # for i in range(0, len(graph)):
    #     graph[i].sort(reverse=True)
    #     # graph[i].reverse는 순서만 거꾸로 바꿔준다!
        
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
"""
list에 빈 list가 들어가있어야 
그 안에 값을 append할 수 있다.

그래서 입력받은 정점의 개수만큼 []를 만들어준다.
"""
for i in range(1, vertex+1):
    graph.append([])

for i in range(1, edge+1):
    v1, v2 = list(map(int, input().split()))
   
    """
    1 2를 입력받은 경우
    list 1에는 2를 넣어주고
    list 2에는 1을 넣어주는 작업
    """    
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(graph, start)
bfs(graph, start)
