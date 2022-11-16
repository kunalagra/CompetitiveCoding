for _ in range(int(input())):
    a1 = list(map(int,input().split()))
    
    if a1[0]/a1[2]>a1[1]/a1[3]:
        print("Chefina")
    elif a1[0]/a1[2]<a1[1]/a1[3]:
        print("Chef")
    else:
        print("Both")