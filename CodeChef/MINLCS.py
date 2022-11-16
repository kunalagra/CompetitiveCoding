from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = Counter(input())
    b = Counter(input())

    ans=0
    for l,c in a.most_common():
        if l in b.keys():
            temp = min(c,b[l])
            ans = max(ans,temp)
    print(ans)