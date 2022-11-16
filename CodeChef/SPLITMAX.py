for x in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    s = sum(l)
    if s>1:
        s = s * (s-1)
    print(s%998244353)