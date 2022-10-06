for _ in range(int(input())):
    n= int(input())
    l=input()
    if len(l)<=2:
        print(l)
    else:
        print(''.join(sorted(l)))
    