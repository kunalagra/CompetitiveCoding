for _ in range(int(input())):
    n = int(input())
    a1 = input()
    f = False
    for x in range(1,len(a1)):
        if a1[x]=='1':
            print(x)
            f =True
            break
    if not f:
        print(n)