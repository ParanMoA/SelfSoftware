N,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for _ in range(K+1)] for _ in range(N)]

for i in range(N) : #row 
  for j in range(K+1) :
    w = arr[i][0]
    v = arr[i][1]    
    if j < w :
      dp[i][j] = dp[i-1][j]
    else :
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
    print("dp[{}][{}] = {}".format(i,j,dp[i][j]))

print(dp[N-1][K])
