for _ in range(int(input())):
    n = int(input())
    s = input()
    ans=""
    l,r=0,n-1
    while(1):
        ans= ans+s[l] if s[l]=='1' else s[l]+ans
        l+=1
        if l>r:
            break
        ans = ans+s[r] if s[r]=='0' else s[r]+ans
        r-=1
        if(l>r):
            break
    print(ans)