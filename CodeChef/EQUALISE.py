from math import log
# cook your dish here
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==b:
        print("YES")
    else:
        v = a/b if a>b else b/a
        if (log(v)/log(2)).is_integer():
            print("YES")
        else:
            print("NO")
        