def recursive(i):
    if i == 11:
        return
    print("재귀함수 호출")
    recursive(i+1)

recursive(1)
