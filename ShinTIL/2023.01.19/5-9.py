#bfs 예제

from collections import deque

def bfs(graph, start, visited):
    #탐색 시작 노드를 큐에 삽입
    queue = deque([start])
    
    #탐색 시작 노드 방문 처리
    visited[start] = True

    while queue:
        #탐색 시작 노드를 큐에서 제거 
        v = queue.popleft()
        print(v, end='')
        
        #해당 노드의 인접 노드들을 하나씩 탐색하여
        for i in graph[v]:
            #방문하지 않은 노드를
            if not visited[i]:
                #큐에 삽입하고
                queue.append(i)
                #해당 노드 방문 처리
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)