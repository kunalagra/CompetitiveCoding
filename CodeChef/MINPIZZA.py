from math import ceil
for _ in range(int(input())):
    n,x = map(int,input().split())
    s = n*x
    print(ceil(s/4))
    