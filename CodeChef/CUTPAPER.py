from math import floor
for _ in range(int(input())):
    n,k = map(int,input().split())
    r = floor(n/k)
    print(r*r)

    