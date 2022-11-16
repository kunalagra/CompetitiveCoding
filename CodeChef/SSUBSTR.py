for _ in range(int(input())):
    n = int(input())
    l = input()
    c = 0
    for x in range(len(l)-1):
        if l[x]== '1' and l[x+1]== '0':
            c+=1
    print(c)