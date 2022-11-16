for _ in range(int(input())):
    n = int(input())
    s = input()
    o = s.count("1")
    ans = min(o,n-o)
    ans+=((o-min(o,n-o))//3)
    print(ans)
