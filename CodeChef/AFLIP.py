# from collections import Counter
for _ in range(int(input())):
    n,m = map(int, input().split())
    al = list()
    bl = list()
    for a in range(n):
        l = list(map(int, input().split()))
        al.append(l)
    for a in range(n):
        l = list(map(int, input().split()))
        bl.append(l)
    if n==1 or m==1:
        if al == bl:
            print("YES")
        else:
            print("NO")
    else:
        ao,ae,bo,be = [],[],[],[]
        for i in range(n):
            for j in range(m):
                if (i+j)&1==0:
                    ae.append(al[i][j])
                    be.append(bl[i][j])
                else:
                    ao.append(al[i][j])
                    bo.append(bl[i][j])

        if (sorted(ae) == sorted(be)) and (sorted(ao)==sorted(bo)):
            print("YES")
        else:
            print("NO")