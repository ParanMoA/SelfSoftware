result =1 

def recursive(n):
    if n <= 1:
        return 1
    return n * recursive(n-1)

print("5! = " + str(recursive(5)))