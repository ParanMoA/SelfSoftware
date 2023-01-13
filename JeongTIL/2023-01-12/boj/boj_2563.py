arr = [[0]*100 for _ in range (100)]
n = int(input())
num = 0

for _ in range(n) :
  row,col = map(int, input().split())
  for i in range(row,row+10) : 
    for j in range (col, col+10):
        arr[i][j] = 1;

for i in range(100):
  num += arr[i].count(1)

print(num)
