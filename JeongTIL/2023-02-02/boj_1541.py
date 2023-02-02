s = input()
arr = s.split('-')
sum = flag = 0
for a in arr :
  brr = a.split('+')
  if flag == 0:
    for b in brr:
      sum += int(b)
  else:
    for b in brr:
      sum -= int(b)
  flag = 1
print(sum)  
