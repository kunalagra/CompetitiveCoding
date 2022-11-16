for _ in range(int(input())):
    n = int(input())
    s = input()
    if s==s[::-1]:
        print("YES")
    else:
        z,o=0,0
        for x in s:
            if x=='0':
                z+=1
            else:
                o+=1
        if z%2 and o%2:
            print("NO")
        else:
            print("YES")