def iterative(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print("5! = " + str(iterative(5)))
    