for _ in range(int(input())):

    s = input()

    N = len(s)
    arr = [0 for _ in range(N)]
    arr[0] = 1
    for i in range(1,N):
        if s[i]!=s[i-1]:
            arr[i] =( arr[i-1] + (arr[i-2] if i>1 else 1))%998244353
        else:
            arr[i] = arr[i-1]%998244353
        
    print(arr[-1])