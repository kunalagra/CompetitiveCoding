for x in range(int(input())):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    dp = [[0 for x in range(n)] for y in range(64)] 
    for x in range(n):
        for y in range(64):
            dp[y][x] = int(arr[x]%2)
            arr[x] = arr[x]//2
    
    for x in range(64):
        c=0
        for y in range(n):
            c+=dp[x][y]
            dp[x][y] =c
    for x in range(q):
        k,l1,r1,l2,r2 = map(int,input().split())
        l1-=1
        l2-=1
        r1-=1
        r2-=1
        t1 = r1-l1+1
        t2 = r2-l2+1
        t11 = dp[k][r1] if l1==0 else dp[k][r1]-dp[k][l1-1]
        t22 = dp[k][r2] if l2==0 else dp[k][r2]-dp[k][l2-1]
        s = (t1-t11)*(t22)+(t11)*(t2-t22)
        print(s)            
        