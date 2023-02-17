import sys
input = sys.stdin.readline

arr = list(input())
m = int(input())

count = len(arr)
for i in range(m):
    a = input().split()
    if a[0] == 'P':
        if count == 0:
            arr.insert(count, a[1])
        else:
            arr.insert(count-1,a[1])
        count += 1
    elif a[0] == 'L':
        if count == 0:
            continue
        else:
            count -= 1
    elif a[0] == 'D':
        if count == len(arr):
            continue
        else:
            count += 1
    elif a[0] == 'B':
        if count == 1:
            continue
        else:
            arr.pop(count-2)
            count -= 1
    # print(arr)
        
for i in arr:
    if i == '0':
        continue
    else:
        print(i, end='')