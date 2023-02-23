x,y = map(int,input().split())
num = 0
for i in range(1,x) :
  if i==4 or i==6 or i==9 or i==11:
    num += 30 % 7
  elif i==2:
    num += 28 % 7
  else:
    num += 31 % 7
num += y%7
num %= 7
day =['MON','TUE','WED','THU','FRI','SAT','SUN']
print(day[num-1])
