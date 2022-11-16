for x in range(int(input())):
    n,k,l = map(int,input().split())
    if k+l<n:
        a = n-(k+l)
        b = (k*l + a*(k+l) ) + ((a*(a-1))//2)
        print(b)
    else:
        print((n-k)*(n-l))