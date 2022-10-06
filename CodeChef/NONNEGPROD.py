for _ in range(int(input())):
    n= int(input())
    l=list(map(int,input().split()))
    if 0 in l:
        print(0)
    else:
        a= sum(1 for i in l if i < 0)
        if a%2==0:
            print(0)
        else:
            print(1)