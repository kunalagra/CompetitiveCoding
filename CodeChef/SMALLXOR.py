# cook your dish here
from heapq import heapify, heappush, heappop,heapreplace

for _ in range(int(input())):
    n,x,y = map(int, input().split())
    l = list(map(int, input().split()))
    heapify(l)
    while(y):
        m = l[0]
        if (m^x)>m:
            heapreplace(l,m^x)
            y-=1
        else:
            if y&1 == 0:
                break
            else:
                heapreplace(l,m^x)
                break
    print(*sorted(l))