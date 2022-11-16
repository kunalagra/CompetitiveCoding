for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    m = max(set(l), key = l.count)
    c=0
    for x in l:
        if x!=m:
            c+=1
    print(c)