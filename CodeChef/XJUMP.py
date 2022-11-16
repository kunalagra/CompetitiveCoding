for _ in range(int(input())):
    x,y =map(int,input().split())
    
    ans = x%y
    ans += (x//y)
    print(ans)