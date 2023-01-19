n,m =  map(int, input().split())
arr = list (map(int, input().split()))
bound_M = max(arr)
bound_m = min(arr)
flag = result = middle = 0

while 1: 
  if flag and middle == result: break
 
  sum = 0
  for a in arr:
    sum += a - middle if a - middle > 0 else 0
 
  bound_m = middle
  if sum >= m:
    flag = 1
    result = middle
  elif flag:
    bound_M = middle
    bound_m = result
  middle = int((bound_M + bound_m)/2)
  
print(middle)
