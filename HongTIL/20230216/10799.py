import sys
input = sys.stdin.readline

arr = list(input())
result = []
count = 0

for i in range(len(arr)):
    if arr[i] == '(':
        result.append(arr[i])
    elif arr[i] == ')':
        if arr[i-1] == '(':
            result.pop()
            count += len(result)
        else:
            result.pop()
            count += 1

print(count)