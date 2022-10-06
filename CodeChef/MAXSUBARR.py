for _ in range(int(input())):
    n1 = int(input())
    a1 = list(map(int,input().split()))
    n2 = int(input())
    a2 = list(map(int,input().split()))
    ms = 0
    s1,s2=0,0
    for i in range(n1):
        s1+=a1[i]
        s2+=a1[n1-i-1]
        ms = max(ms,s1,s2)
    for i in range(n2):
        if a2[i]>0:
            ms+=a2[i]
    print(ms)
    