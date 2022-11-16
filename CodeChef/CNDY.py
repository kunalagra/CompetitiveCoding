from collections import Counter
for x in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    c=Counter(arr).values()
    f=0
    for x in c:
        if x>2:
            f=1
            break
    if f:
        print("No")
    else:
        print("Yes")
            
