for _ in range(int(input())):
    a,b= map(int,input().split())
    if ((a%2) and (b%2)) or (a==1) or (b==1):
        print("No")
    else:        
        print("Yes")