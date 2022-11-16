for x in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    f=0
    if n==1 and k in arr:
        f=0
    elif k not in arr:
        f=1
    elif arr[-1]==k and (k not in arr[:-1]):
        f=1
    
    if f:
        print('No')
    else:
        print("Yes")