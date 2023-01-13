M = 0
for i in range(9):
  arr = list(map(int, input().split()))
  m = max(arr)
  if m >= M:
    M = m 
    row = i
    col = arr.index(M)
print(M)
print(row+1," ",col+1)
