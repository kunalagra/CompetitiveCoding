for _ in range(int(input())):
    x,y = map(int,input().split())
    s = "YES"  if y/x>=.5 else "NO"
    print(s)