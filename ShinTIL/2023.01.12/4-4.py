n, m = map(int, input().split())
x, y, d = map(int, input().split())
cnt = 0
sign = True

game_map = [[-1 for i in range(m)] for j in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    game_map[i] = list(map(int, input().split()))

while sign == True:
    for i in range(4):
        d -= 1
        if d < 0:
            d = 3
        
        new_x = x + dx[d] 
        new_y = y + dy[d]

        if game_map[new_x][new_y] != 1:
            continue
        else:
            x = new_x
            y = new_y
            game_map[x][y] = 2
            cnt += 1
    new_x = x - dx[d]
    new_y = y - dy[d]

    if game_map[new_x][new_y] == 1:
        sign = False
    
    x = new_x
    y = new_y

print(cnt)