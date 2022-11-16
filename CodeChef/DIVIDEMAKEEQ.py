for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    m = min(l)
    cnt=0
    f=0
    for x in l:
        if x%m==0:
            if x//m!=1:
                cnt+=1
        else:
            f=1
            break
    if f:
        print(n)
    else:
        print(cnt)