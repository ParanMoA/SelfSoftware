n = int(input())
a = n
b = -1
num = 0
while b != n:
  num += 1
  b = (int)(a/10) + (a%10)
  b = (a%10)*10 + (b%10)
  a = b
print(num)
