from math import ceil
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    m = n//2
    a1 = l[:m]
    a1 = a1[::-1]
    a2 = l[m+1:] if n&1 else l[m:]
    diff = list()
    for i in range(len(a1)):
        diff.append(a2[i]-a1[i])
    f=False
    for x in diff:
        if x<0:
            f=True
    for x in range(1,len(diff)):
        if diff[x]<diff[x-1]:
            f=True
    if f:
        print(-1)
    else:
        print(diff[-1])