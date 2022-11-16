for _ in range(int(input())):
    n = int(input())
    s = input()
    c=0
    prev=""
    for x in s:
        if x!=prev:
            prev=x
        else:
            c+=1
    print(c)