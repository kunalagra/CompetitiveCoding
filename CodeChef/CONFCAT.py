for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    f = False
    i = 0
    for x in range(1,n):
        if l[x]>l[0]:
            f = True
            i = x
            break
    if not f:
        print(-1)
    else:
        print(i)
        print(*l[:i])
        print(n-i)
        print(*l[i:])