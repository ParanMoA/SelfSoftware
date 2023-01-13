N,M = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N)]
b = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
  c = [x + y for x,y in zip(a[i],b[i])]
  for j in range(M):
    print(c[j],end=' ')
  print()
