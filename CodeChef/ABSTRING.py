from collections import Counter
for x in range(int(input())):
    n  = int(input())
    s = input()
    c = Counter(s).values()
    f=0
    for x in c:
        if x%2!=0:
            f=1
            break

    print("NO" if f else "YES")
