for _ in range(int(input())):
    a,b =  map(int,input().split())

    if (b-a)>=a or a==b:
        print("YES")
    else:
        print("NO")