for _ in range(int(input())):
    l = list(map(int,input().split()))
    if l[2]%l[1]==0:
        print("YES")
    else:
        print("NO")