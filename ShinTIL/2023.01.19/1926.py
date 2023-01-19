n, m = map(int, input().split())
graph = []
arr = []
cnt = 0

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    global cnt
    if x<0 or y<0 or x>=n or y>=m:
        return False
    
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        value = cnt
        cnt = 0
        return True

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            arr.append(cnt)
            result += 1
print(max(arr))

print(result)