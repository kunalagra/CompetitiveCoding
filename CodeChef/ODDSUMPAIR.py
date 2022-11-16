for _ in range(int(input())):
    l = list(map(int,input().split()))
    c = 0
    for x in l:
        if x%2==0:
            c+=1
    if c==1 or c ==2:
        print("YES")
    else:
        print("NO")