for _ in range(int(input())):
    n,q =  map(int,input().split())
    l = list(map(int,input().split()))
    ans = sum(l)
    for x in range(q):
        l,r = map(int,input().split())
        if ((r-l)+1)%2!=0:
            ans+=1
    print(ans)